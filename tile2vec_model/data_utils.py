'''
This code is modified from https://github.com/ermongroup/tile2vec/blob/master/src/data_utils.py
'''
import numpy as np


def clip_and_scale_image(img, img_type='airbus', clip_min=0, clip_max=10000,
                         max_ax1=90, max_ax2=87):
    """
    Clips and scales bands to between [0, 1] for NAIP, RGB, and Landsat
    satellite images. Clipping applies for Landsat only.
    Assume image is 3D array of form (c, w, h) or (c, h, w).
    """
    if img_type in ['naip', 'rgb']:
        return img / 255
    elif img_type == 'airbus':
        img = img[:, :max_ax1, :max_ax2]
        min_ = img.min((1, 2))
        scale = img.max((1, 2)) - min_ + 0.000000001
        bias = np.einsum('ijk, i -> ijk', np.ones(img.shape), min_)
        return np.einsum('ijk, i -> ijk', img - bias, 1 / scale)
    elif img_type == 'landsat':
        return np.clip(img, clip_min, clip_max) / (clip_max - clip_min)
