# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/06_datasets.ipynb.

# %% auto 0
__all__ = ['VideoFrameDataset']

# %% ../nbs/06_datasets.ipynb 2
import torch.utils.data as td
from avcv.all import *

class VideoFrameDataset(td.Dataset):
    def __init__(self, path_to_video, img_preproc=None, out_dir=None, img_size=(416, 416), fps=10):
        if out_dir is None:
            vname = get_name(path_to_video)
            out_dir = f'/tmp/ple/VideoFrameDataset/extracted_video_for_inference/{vname}_fps_{fps}'
        self.out_dir = out_dir
        self.img_preproc = img_preproc
        self.fps = fps
        self.img_size = img_size
        self.video = mmcv.VideoReader(path_to_video)
        self.paths = self.get_images(path_to_video)
    
    def __len__(self):
        return len(self.paths)
    
    def __getitem__(self, idx):
        img = mmcv.imread(self.paths[idx])
        if self.img_preproc is not None:
            x = self.img_preproc(img)[0][0]
            return dict(x=x, img=img)
        return dict(img=img)
    
    def get_images(self, path_to_video):
        if not self.check_if_extracted(path_to_video):
            _im = mmcv.imrescale(self.video[0], self.img_size)
            im_h, im_w = _im.shape[:2]
            mmcv.mkdir_or_exist(self.out_dir)
            cmd = f"ffmpeg -n  -i {path_to_video} -s {im_w}x{im_h} -vf fps={self.fps} {self.out_dir}/%06d.jpg "
            print(cmd)
            os.system(cmd)
#         else:
#             print('Skip extracting using ffmpeg since files are already extracted')
        paths = glob(f'{self.out_dir}/*.jpg')
        return list(sorted(paths))
    
    def check_if_extracted(self, path_to_video):
        exist_num = len(glob(f'{self.out_dir}/*.jpg'))
        expected_num = len(self.video)*self.fps/self.video.fps
        exist_rate = exist_num/expected_num
        if exist_rate<0.9:
            print(f'{exist_rate=}')
        return exist_rate>0.9

