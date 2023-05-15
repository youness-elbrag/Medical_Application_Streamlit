from subprocess import list2cmdline
import Augmentor
import os
import PIL
import time
import cv2
import glob

from cv2 import USAGE_ALLOCATE_HOST_MEMORY
from cv2 import resize
from numpy import append
# Create a pipeline
ORIGIN_MERGED_SOURCE_DIRECTORY = "./Cropped_Images"
# p = Augmentor.Pipeline(path_to_data)
TRAIN_SET_SIZE = 300
VALIDATION_SET_SIZE = 150
TEST_SET_SIZE = 90
DIM = (64, 64)

# os.mkdir('./scrapdataset/augment_images/')
AUGMENT_OUTPUT_DIRECTORY = 'Cropped_Images/dataset/augment_images'


def augment():
    p = Augmentor.Pipeline(
        source_directory=ORIGIN_MERGED_SOURCE_DIRECTORY,
        output_directory=AUGMENT_OUTPUT_DIRECTORY
    )
    p.rotate(probability=0.02, max_left_rotation=2, max_right_rotation=2)
    p.zoom(probability=0.02, min_factor=1.1, max_factor=1.2)
    p.skew(probability=0.02)
    # p.random_distortion(probability=0.2, grid_width=100, grid_height=100, magnitude=1)
    p.shear(probability=0.02, max_shear_left=2, max_shear_right=2)
    p.crop_random(probability=0.02, percentage_area=0.7)
    p.flip_random(probability=0.4)
    p.sample(n=TRAIN_SET_SIZE + VALIDATION_SET_SIZE + TEST_SET_SIZE)
#listfolders = []


# def move_augmented_images():
#     output = './scrapdataset/resized'
#     paths = os.listdir(AUGMENT_OUTPUT_DIRECTORY)
#     if not os.path.lexists(output):
#         os.mkdir(output)
#     for j in paths:
#         subpath = os.path.join(AUGMENT_OUTPUT_DIRECTORY, j)
#         listfolders.append(subpath)
#         print(subpath)
#         for index in listfolders:
#             input_img =glob.glob(os.path.join(index+ '/*.jpg'))
#             #print(input_img)
#             for name_img , input_img in enumerate(input_img):
#                 path_class=os.path.move(output,input_img[name_img].split('/')[:-1])
#                 if not os.path.lexists(path_class):
#                     os.mkdir(path_class)
#                 image = cv2.imread(input_img, cv2.IMREAD_UNCHANGED)
#                 resize = (image, (64, 64), cv2.INTER_AREA)
#                 filename = os.path.join(output, str(name_img)+'.jpg')
#                 cv2.imwrite(filename,resize)


if __name__ == '__main__':
    augment()
    #move_augmented_images()
