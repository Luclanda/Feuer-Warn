# Feuer-Warn
Feuer-Warn is a system that utilizes object detection to warn people through a localhost. The object detection model is a Yolov8 m. 

Feuer-Warn is made for Raspberry Pi, but you can also use it in Jupyter Notebook on a PC or Mac. You need to run the command ```libcamera-vid -n -t 0 --width 1280 --height 960 --framerate 1 --inline --listen -o tcp://127.0.0.1:8888``` to start the camera. If desired, you can also execute the yolo.py code from another device, but in that case, you must specify the command for the terminal.

To run the python code, you need to make sure that the Yolov8 model is downloaded and under the right path.

