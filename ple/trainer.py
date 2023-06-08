# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/05_trainer.ipynb.


from fastcore.utils import *
from fastcore.script import *
import shutil
import os
__all__ = ['is_interactive', 'get_trainer',
           'get_rank', 'get_exp_by_file', 'train']


import os.path as osp

from loguru import logger
from pytorch_lightning import Trainer
from pytorch_lightning.callbacks import LearningRateMonitor, ModelCheckpoint
from pytorch_lightning.callbacks.progress import TQDMProgressBar
from pytorch_lightning.loggers import TensorBoardLogger
import torch

def is_interactive():
    try:
        shell = get_ipython().__class__.__name__
        return True
    except:
        return False

def get_trainer(exp_name=None,
                max_epochs=None,
                gpus=1,
                monitor=dict(metric="val_loss", mode="min"),
                save_every_n_epochs=1,
                save_top_k=1,
                strategy='auto',
                accelerator='gpu',
                refresh_rate=5,
                **kwargs)->Trainer:
    if not torch.cuda.is_available():
        gpus = 1
        accelerator = 'cpu'
        logger.warning(
            "No GPU available, using CPU instead, gpus=1, accelerator='cpu'")

    callbacks = []
    plt_logger = None
    if exp_name is not None:
        rld = osp.join("lightning_logs", exp_name)
        cur_num_exps = len(os.listdir(rld)) if osp.exists(rld) else 0
        version = f"{cur_num_exps:02d}"
        root_log_dir = osp.join("lightning_logs", exp_name, version)
        if monitor is None:
            filename = None
        else:
            filename = "{epoch}_{"+monitor["metric"]+":0.4f}"

        callback_ckpt = ModelCheckpoint(
            dirpath=osp.join(root_log_dir),
            monitor=monitor['metric'] if monitor is not None else None,
            mode=monitor['mode'] if monitor is not None else 'min',
            filename=filename,
            save_last=True,
            every_n_epochs=save_every_n_epochs,
            save_top_k=save_top_k,
        )
        class CustomTensorBoardLogger(TensorBoardLogger):
            @property
            def log_dir(self):
                ld = super().log_dir
                return ld.split('/version')[0]

        plt_logger = CustomTensorBoardLogger(
            osp.join(root_log_dir),
        )
        callbacks.append(callback_ckpt)

    callbacks.append(TQDMProgressBar(refresh_rate=refresh_rate))
    callbacks.append(LearningRateMonitor(logging_interval="step"))

    if strategy is None:
        if is_interactive():
            logger.info("gpus={}, Interactive mode, force strategy=auto", gpus)
            strategy = 'auto'
        elif gpus < 2:
            logger.info("gpus={}, , force strategy=dp", gpus)
            strategy = 'auto'
        else:
            strategy = "ddp"
            logger.info(
                "gpus={}, strategy=ddp, set strategy='dp' if this", gpus)
    if 'strategy' == 'ddp':
        from pytorch_lightning.strategies.ddp import DDPStrategy
        strategy = DDPStrategy(find_unused_parameters=False)
    trainer = Trainer(
        accelerator=accelerator,
        devices=gpus,
        max_epochs=max_epochs,
        strategy=strategy,
        callbacks=callbacks,
        log_every_n_steps=refresh_rate,
        logger=plt_logger, **kwargs
    )
    return trainer


# # from argparse import ArgumentParser
# from pytorch_lightning import Trainer, seed_everything
# # from ple.all import get_trainer, BaseExp


def get_rank() -> int:
    import torch.distributed as dist
    if not dist.is_available():
        return 0
    if not dist.is_initialized():
        return 0
    return dist.get_rank()


def get_exp_by_file(exp_file):
    """
        Params:
        exp_file: Path to exp

    """
    try:
        import importlib
        import os
        import sys
        sys.path.append(os.path.dirname(exp_file))
        # import ipdb; ipdb.set_trace()
        current_exp = importlib.import_module(
            os.path.basename(exp_file).split(".")[0])
        current_exp = importlib.reload(current_exp)
        exp = current_exp.Exp()
        return exp
    except Exception:
        raise ImportError(
            "{} doesn't contains class named 'Exp'".format(exp_file))


@call_parse
def train(
    cfg_path: Param('Path to config'),
    devices: Param('GPUS indices', default=1, type=int),
    accelerator: Param('cpu or gpu', default='gpu', type=str),
    opts: Param('Additional configs', default='', type=str, required=False),
):
    cfg = get_exp_by_file(cfg_path)
    if len(opts):
        cfg.merge(opts.replace('=', ' ').split(' '))
    cfg.devices = devices

    data = cfg.get_data_loader()

    model = cfg.get_model(create_lr_scheduler_fn=cfg.get_lr_scheduler(),
                          create_optimizer_fn=cfg.get_optimizer())
    trainer = cfg.get_trainer(devices)
    try:
        trainer.fit(model, data)
    except Exception as e:
        import traceback
        traceback.print_exc()
    finally:
        if get_rank() == 0:
            out_path = osp.join(trainer.log_dir, osp.basename(cfg_path))
            logger.info('cp {} {}', cfg_path, out_path)
            shutil.copy(cfg_path, out_path)
