import mrcnn
import mrcnn.config
import mrcnn.model
import mrcnn.visualize
import cv2
import os
import skimage
from mrcnn import utils
# load the class label names from disk, one label per line
# CLASS_NAMES = open("coco_labels.txt").read().strip().split("\n")

CLASS_NAMES = ['background','cell']

class SimpleConfig(mrcnn.config.Config):
    # Give the configuration a recognizable name
    NAME = "coco_inference"
    
    # set the number of GPUs to use along with the number of images per GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

	# Number of classes = number of classes + 1 (+1 for the background). The background class is named BG
    NUM_CLASSES = len(CLASS_NAMES)

# Initialize the Mask R-CNN model for inference and then load the weights.
# This step builds the Keras model architecture.
model = mrcnn.model.MaskRCNN(mode="inference", 
                             config=SimpleConfig(),
                             model_dir=os.getcwd())

# Load the weights into the model.
# model.load_weights(filepath="mask_rcnn_coco.h5",
#                    by_name=True)
model.load_weights(filepath="cell-learning/image=980/mask_rcnn_cell_cfg_0001.h5",
                   by_name=True)

# load the input image, convert it from BGR to RGB channel
IMAGE_DIR = 'Result/test_pic'
count = os.listdir(IMAGE_DIR)
for i in range(0,len(count)):
    path = os.path.join(IMAGE_DIR, count[i])
    if os.path.isfile(path):
        file_names = next(os.walk(IMAGE_DIR))[2]
        image = skimage.io.imread(os.path.join(IMAGE_DIR, count[i]))
        # Run detection
        results = model.detect([image], verbose=1)
        r = results[0]
        mrcnn.visualize.display_instances(count[i],
                                          image=image,
                                          boxes=r['rois'],
                                          masks=r['masks'],
                                          class_ids=r['class_ids'],
                                          out_json=False,
                                          class_names=CLASS_NAMES,
                                          scores=r['scores'])

