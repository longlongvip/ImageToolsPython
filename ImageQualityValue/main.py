import cv2
import numpy as np
from skimage import img_as_float
from skimage.measure import compare_psnr, compare_ssim

im_path_noise = 'NoiseFace/6.jpg'
im_path_de_noise = 'DeNoiseFace/6.jpg'

im_noisy = img_as_float(cv2.imread(im_path_noise)[:, :, ::-1])
im_noisy = im_noisy.astype(np.float32)


im_de_noise = img_as_float(cv2.imread(im_path_de_noise)[:, :, ::-1])
im_de_noise = im_de_noise.astype(np.float32)

psnr_val = compare_psnr(im_noisy, im_de_noise, data_range=255)
ssim_val = compare_ssim(im_noisy, im_de_noise, data_range=255, multichannel=True)

print('PSNR={:5.2f}, SSIM={:7.4f}'.format(psnr_val, ssim_val))
