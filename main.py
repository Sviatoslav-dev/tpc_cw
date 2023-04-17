import math
import time

import numpy as np
from PIL import Image


def gaussian_function(x, y, sigma):
    return ((1.0 / (2 * math.pi * sigma ** 2))
            * math.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2)))


def generate_gaussian_kernel(size, sigma):
    offset = size // 2
    kernel = np.zeros((size, size))
    for x in range(-offset, offset + 1):
        for y in range(-offset, offset + 1):
            kernel[x + offset, y + offset] = gaussian_function(x, y, sigma)
    return kernel / np.sum(kernel)


def apply_convolution(image, kernel):
    height, width, channels = image.shape
    kernel_size = kernel.shape[0]
    offset = kernel_size // 2
    blurred_image = np.zeros_like(image, dtype=np.float32)

    for c in range(channels):
        for x in range(offset, width - offset):
            for y in range(offset, height - offset):
                window = image[y - offset:y + offset + 1,
                               x - offset:x + offset + 1,
                               c]
                blurred_image[y, x, c] = np.sum(window * kernel)

    return blurred_image.astype(np.uint8)


image_path = 'image_512x512.jpg'

image = Image.open(image_path)
image_data = np.array(image)

kernel_size = 15
sigma = 5.0

gaussian_kernel = generate_gaussian_kernel(kernel_size, sigma)
print(np.around(gaussian_kernel, 2))

start = time.time()
blurred_image_data = apply_convolution(image_data, gaussian_kernel)
print("execution time: {} seconds".format(time.time() - start))

blurred_image = Image.fromarray(blurred_image_data)
blurred_image.show()
