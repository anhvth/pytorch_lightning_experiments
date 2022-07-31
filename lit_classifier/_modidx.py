# Autogenerated by nbdev

d = { 'settings': { 'audience': 'Developers',
                'author': 'anhvth',
                'author_email': 'anhvth.226@gmail.com',
                'branch': 'main',
                'copyright': 'https://github.com/anhvth',
                'custom_sidebar': 'False',
                'description': '"Wraper for pytorch lighining classification"',
                'doc_baseurl': '/lit_classifier/',
                'doc_host': 'https://anhvth.github.io',
                'doc_path': 'docs',
                'git_url': 'https://github.com/anhvth/lit_classifier/tree/main/',
                'host': 'github',
                'keywords': 'fast pytorch classifie builder',
                'language': 'English',
                'lib_name': 'lit_classifier',
                'lib_path': 'lit_classifier',
                'license': 'apache2',
                'min_python': '3.6',
                'nbs_path': './nbs/',
                'recursive': 'False',
                'requirements': 'timm pytorch_lightning loguru mmcv loguru tabulate',
                'status': '2',
                'title': 'lit_classifier',
                'user': 'anhvth',
                'version': '0.0.2'},
  'syms': { 'lit_classifier.all': {},
            'lit_classifier.base_exp': { 'lit_classifier.base_exp.BaseExp': 'https://anhvth.github.io/lit_classifier/base_exp.html#baseexp',
                                         'lit_classifier.base_exp.BaseExp.get_data_loader': 'https://anhvth.github.io/lit_classifier/base_exp.html#baseexp.get_data_loader',
                                         'lit_classifier.base_exp.BaseExp.get_lr_scheduler': 'https://anhvth.github.io/lit_classifier/base_exp.html#baseexp.get_lr_scheduler',
                                         'lit_classifier.base_exp.BaseExp.get_model': 'https://anhvth.github.io/lit_classifier/base_exp.html#baseexp.get_model',
                                         'lit_classifier.base_exp.BaseExp.get_optimizer': 'https://anhvth.github.io/lit_classifier/base_exp.html#baseexp.get_optimizer'},
            'lit_classifier.lit_model': { 'lit_classifier.lit_model.LitModel': 'https://anhvth.github.io/lit_classifier/lit_model.html#litmodel',
                                          'lit_classifier.lit_model.LitModel.configure_optimizers': 'https://anhvth.github.io/lit_classifier/lit_model.html#litmodel.configure_optimizers',
                                          'lit_classifier.lit_model.LitModel.forward': 'https://anhvth.github.io/lit_classifier/lit_model.html#litmodel.forward',
                                          'lit_classifier.lit_model.LitModel.training_step': 'https://anhvth.github.io/lit_classifier/lit_model.html#litmodel.training_step',
                                          'lit_classifier.lit_model.LitModel.validation_step': 'https://anhvth.github.io/lit_classifier/lit_model.html#litmodel.validation_step',
                                          'lit_classifier.lit_model.fn_schedule_cosine_with_warmpup_decay_timm': 'https://anhvth.github.io/lit_classifier/lit_model.html#fn_schedule_cosine_with_warmpup_decay_timm',
                                          'lit_classifier.lit_model.fn_schedule_linear_with_warmup': 'https://anhvth.github.io/lit_classifier/lit_model.html#fn_schedule_linear_with_warmup',
                                          'lit_classifier.lit_model.get_scheduler': 'https://anhvth.github.io/lit_classifier/lit_model.html#get_scheduler',
                                          'lit_classifier.lit_model.get_trainer': 'https://anhvth.github.io/lit_classifier/lit_model.html#get_trainer',
                                          'lit_classifier.lit_model.plot_lr_step_schedule': 'https://anhvth.github.io/lit_classifier/lit_model.html#plot_lr_step_schedule'},
            'lit_classifier.loss': { 'lit_classifier.loss.BinaryFocalLoss': 'https://anhvth.github.io/lit_classifier/loss.html#binaryfocalloss',
                                     'lit_classifier.loss.BinaryFocalLoss.forward': 'https://anhvth.github.io/lit_classifier/loss.html#binaryfocalloss.forward',
                                     'lit_classifier.loss.FocalLoss': 'https://anhvth.github.io/lit_classifier/loss.html#focalloss',
                                     'lit_classifier.loss.FocalLoss.forward': 'https://anhvth.github.io/lit_classifier/loss.html#focalloss.forward',
                                     'lit_classifier.loss.py_sigmoid_focal_loss': 'https://anhvth.github.io/lit_classifier/loss.html#py_sigmoid_focal_loss',
                                     'lit_classifier.loss.reduce_loss': 'https://anhvth.github.io/lit_classifier/loss.html#reduce_loss',
                                     'lit_classifier.loss.sigmoid_focal_loss': 'https://anhvth.github.io/lit_classifier/loss.html#sigmoid_focal_loss',
                                     'lit_classifier.loss.weight_reduce_loss': 'https://anhvth.github.io/lit_classifier/loss.html#weight_reduce_loss'},
            'lit_classifier.persistance': { 'lit_classifier.persistance.EasyDict': 'https://anhvth.github.io/lit_classifier/persistance.html#easydict',
                                            'lit_classifier.persistance.Logger': 'https://anhvth.github.io/lit_classifier/persistance.html#logger',
                                            'lit_classifier.persistance.Logger.close': 'https://anhvth.github.io/lit_classifier/persistance.html#logger.close',
                                            'lit_classifier.persistance.Logger.flush': 'https://anhvth.github.io/lit_classifier/persistance.html#logger.flush',
                                            'lit_classifier.persistance.Logger.write': 'https://anhvth.github.io/lit_classifier/persistance.html#logger.write',
                                            'lit_classifier.persistance.ask_yes_no': 'https://anhvth.github.io/lit_classifier/persistance.html#ask_yes_no',
                                            'lit_classifier.persistance.call_func_by_name': 'https://anhvth.github.io/lit_classifier/persistance.html#call_func_by_name',
                                            'lit_classifier.persistance.construct_class_by_name': 'https://anhvth.github.io/lit_classifier/persistance.html#construct_class_by_name',
                                            'lit_classifier.persistance.copy_files_and_create_dirs': 'https://anhvth.github.io/lit_classifier/persistance.html#copy_files_and_create_dirs',
                                            'lit_classifier.persistance.format_time': 'https://anhvth.github.io/lit_classifier/persistance.html#format_time',
                                            'lit_classifier.persistance.get_dtype_and_ctype': 'https://anhvth.github.io/lit_classifier/persistance.html#get_dtype_and_ctype',
                                            'lit_classifier.persistance.get_module_dir_by_obj_name': 'https://anhvth.github.io/lit_classifier/persistance.html#get_module_dir_by_obj_name',
                                            'lit_classifier.persistance.get_module_from_obj_name': 'https://anhvth.github.io/lit_classifier/persistance.html#get_module_from_obj_name',
                                            'lit_classifier.persistance.get_obj_by_name': 'https://anhvth.github.io/lit_classifier/persistance.html#get_obj_by_name',
                                            'lit_classifier.persistance.get_obj_from_module': 'https://anhvth.github.io/lit_classifier/persistance.html#get_obj_from_module',
                                            'lit_classifier.persistance.get_top_level_function_name': 'https://anhvth.github.io/lit_classifier/persistance.html#get_top_level_function_name',
                                            'lit_classifier.persistance.import_hook': 'https://anhvth.github.io/lit_classifier/persistance.html#import_hook',
                                            'lit_classifier.persistance.is_persistent': 'https://anhvth.github.io/lit_classifier/persistance.html#is_persistent',
                                            'lit_classifier.persistance.is_pickleable': 'https://anhvth.github.io/lit_classifier/persistance.html#is_pickleable',
                                            'lit_classifier.persistance.is_top_level_function': 'https://anhvth.github.io/lit_classifier/persistance.html#is_top_level_function',
                                            'lit_classifier.persistance.is_url': 'https://anhvth.github.io/lit_classifier/persistance.html#is_url',
                                            'lit_classifier.persistance.list_dir_recursively_with_ignore': 'https://anhvth.github.io/lit_classifier/persistance.html#list_dir_recursively_with_ignore',
                                            'lit_classifier.persistance.make_cache_dir_path': 'https://anhvth.github.io/lit_classifier/persistance.html#make_cache_dir_path',
                                            'lit_classifier.persistance.open_url': 'https://anhvth.github.io/lit_classifier/persistance.html#open_url',
                                            'lit_classifier.persistance.persistent_class': 'https://anhvth.github.io/lit_classifier/persistance.html#persistent_class',
                                            'lit_classifier.persistance.set_cache_dir': 'https://anhvth.github.io/lit_classifier/persistance.html#set_cache_dir',
                                            'lit_classifier.persistance.tuple_product': 'https://anhvth.github.io/lit_classifier/persistance.html#tuple_product'}}}