import os

v_path = 'D:/DeepLearningData/HMDB51/hmdb51_org'
t_path = './hmdb_classes.txt'

f = open(t_path, 'w')

for file in os.listdir(v_path):
    class_name = file.split('.')[0]
    f.write(class_name + '\n')

f.close()
