# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_base_model.ipynb (unless otherwise specified).

__all__ = ['BaseClassifier', 'TimmModelClassifier', 'ClipModelClassifier', 'model_factory', 'test']

# Cell
from abc import ABCMeta, abstractmethod
import numpy as np
import torch.nn as nn
import pytorch_lightning as pl
import timm
import torch
import torch.nn.functional as F
from loguru import logger

class BaseClassifier(nn.Module, metaclass=ABCMeta):
    @abstractmethod
    def extract_features(self, imgs):
        "Extract image features"
        pass

    @abstractmethod
    def forward(self, imgs):
        "Return logits and features"
        pass


class TimmModelClassifier(BaseClassifier):
    def __init__(self, model_name, num_classes=None, pretrained=True, **kwargs):
        self.model_name = model_name
        super(TimmModelClassifier, self).__init__()

        self.base_model = timm.create_model(model_name, pretrained=pretrained, **kwargs)

        self.global_pool = self.base_model.global_pool

        if num_classes is not None:
            nc_in = self._get_nc_in()
            self.classifier = nn.Linear(nc_in, num_classes)

    def _get_nc_in(self):
        # Get num input channel
        if hasattr(self.base_model, "fc"):
            nc_in = self.base_model.fc.in_features
        elif hasattr(self.base_model, "classifier"):
            nc_in = self.base_model.classifier.in_features
        else:
            raise NotImplementedError(self.model_name)
        return nc_in

    def extract_features(self, imgs):
        return self.base_model.forward_features(imgs)

    def forward(self, x):
        features = self.extract_features(x)
        features = self.global_pool(features)
        logits = self.classifier(features)
        return logits, features


class ClipModelClassifier(BaseClassifier):
    def __init__(self, num_classes):
        super().__init__()
        import torch
        import clip

        self.model, self.preprocess = clip.load("ViT-B/32", 'cpu')

        nc_in = self._get_nc_in()
        self.classifier = nn.Linear(nc_in, num_classes)

    def _get_nc_in(self):
        from PIL import Image
        sample = np.random.randint([224, 224, 3]).astype('uint8')
        image = self.preprocess(Image.fromarray(sample)).unsqueeze(0)
        features = self.extract_features(image)
        return features.shape[1]


    def extract_features(self, x):
        with torch.no_grad():
            image_features = self.model.encode_image(x)
        return image_features

    def forward(self, x):
        features = self.extract_features(x)
        logits = self.classifier(features)
        return logits, features


def model_factory(model_name, num_classses)->BaseClassifier:
    logger.info("Init model {}".format(model_name))
    if timm.is_model_pretrained(model_name):
        classifer = TimmModelClassifier(model_name, num_classses)
    else:
        raise NotImplementedError
    return classifer

def test():
    model = ClipModelClassifier(4)
    x = torch.randn(1,3,224,224)
    y_lit = model(x)

    model = model_factory('resnet50', 4)
    y_res = model(x)
    return True