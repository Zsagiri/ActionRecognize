#import tensorflow as tf
from utils import utils
from utils import models


def _main():
    videos_path = './dataset/hmdb51/Main/train.txt'
    classes_path = './model_data/hmdb_classes.txt'
    class_name = get_classes(classes_path)
    input_frames = 10
    input_shape = (320, 320)
    model = creat_model(input_frames, input_shape, len(class_name), load_pretrained=False)
    train()


def train():
    pass


def get_classes(classes_path):
    with open(classes_path) as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    return class_names


def creat_model(input_frames, input_shape, num_classes, load_pretrained=False):
    pass


if __name__ == "__main__":
    _main()
