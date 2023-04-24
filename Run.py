import subprocess
import keyboard
import sys
from threading import Thread


import Yolov5_DeepSort_Pytorch.RunTrack as RT


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        if self.name == 'run':
            run()


videos = ['0',
          'https://www.youtube.com/watch?v=SsvM80bIA1k&ab_channel=MORGENSHTERN',
          'https://www.youtube.com/watch?v=wDsU4H2w48k&ab_channel=MORGENSHTERN'
          ]


def runOld():
    # path = 'C:/Users/CL/PycharmProjects/Biometry/yolov5/runs/train/exp/weights/yolov5s.pt'
    path = 'C:/Users/CL/PycharmProjects/Biometry/yolov5/bestv1.pt'
    source = videos[1]
    device = 'cpu' if source == '0' else '4'
    subprocess.call(f'python yolov5/detect.py --weights {path} --img 416 --conf 0.1 --source {source} --device {device}', shell=True)
    #--device {device}


def run():
    path = 'best1.pt'
    #path = 'C:/Users/CL/PycharmProjects/Biometry/yolov5/runs/train/exp/weights/best1.pt'
    source = videos[1]
    runOld()
    # RT.run(path, source)
    #device = 'cpu' if source == '0' else '4'
    # subprocess.run('cd Yolov5_DeepSort_Pytorch', shell = True)
    # subprocess.run(f'python track.py --yolo_model {path} --img 416 --source {source} --classes 0', shell=True)
    #--device {device}


def close():
    while True:
        if keyboard.is_pressed("q"):
            print("q pressed, ending loop")
            sys.exit()


def main():
    newThread = MyThread('run')
    newThread.daemon = True
    newThread.start()

    keyboard.wait('q')
    sys.exit()


if __name__ == '__main__':
    runOld()


#python yolov5/train.py --img 416 --batch 16 --epochs 150 --data C:/Users/CL/PycharmProjects/Biometry/Biometry-1/data.yaml --weights C:/Users/CL/PycharmProjects/Biometry/yolov5/runs/train/exp/weights/best1.pt --cache
#python train.py --img 416 --batch 16 --epochs 150 --data Biometry-1/data.yaml --weights runs/train/exp/weights/best1.pt --cache

