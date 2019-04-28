import os
import random
import numpy as np
import cv2

train_percent = 0.9
val_percent = 0.1

videos_root = os.path.join(os.getcwd(), 'Videos')
txt_save_path = './Main'
videos_dirs = os.listdir(videos_root)

fTrainVal = open('./Main/trainval.txt', 'w')
fTrain = open('./Main/train.txt', 'w')
n = 0


def get_frames_num(path):
    cap = cv2.VideoCapture(path)
    num_f = int(cap.get(7))
    return num_f


for file in videos_dirs:
    p = os.path.join(videos_root, file)
    video_list = os.listdir(p)
    num = len(video_list)
    List = []
    for i in range(num):
        List.append(i)
    L = List
    np.random.shuffle(L)
    tv = int(num * val_percent)
    trainVal = random.sample(L, tv)

    for i in List:
        n += 1
        video_path = os.path.join(p, video_list[i])
        num_frames = get_frames_num(video_path)
        if i in trainVal:
            fTrainVal.write(video_path + ' ' + str(num_frames) + ' ' + str(videos_dirs.index(file)) + '\n')
        else:
            fTrain.write(video_path + ' ' + str(num_frames) + ' ' + str(videos_dirs.index(file)) + '\n')

fTrainVal.close()
fTrain.close()
print(n)
