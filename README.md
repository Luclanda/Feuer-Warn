# EN:
# Feuer-Warn
Feuer-Warn is a system that utilizes object detection to warn people through a localhost. The object detection model is a Yolov8 m. 

Feuer-Warn is made for Raspberry Pi, but you can also use it in Jupyter Notebook on a PC or Mac. You need to run the command `libcamera-vid -n -t 0 --width 1280 --height 960 --framerate 1 --inline --listen -o tcp://127.0.0.1:8888` if you want to start a Raspberry Pi camera. If you want, you can also run the yolo.py code from another device, but in that case, you must specify the command for the terminal.

To run the Python code, make sure that the YOLOv8 model is downloaded and located in the correct path. Before running the code, make sure you have installed all dependencies.


# DE:
# Feuer-Warn
Feuer-Warn ist ein System, welches Objekterkennung verwendet, um Menschen mithilfe eines localhosts zu warnen. Das Objekterkennungsmodell ist ein Yolov8m.

Feuer-Warn ist für Raspberry Pi entwickelt, kann aber auch in einem Notebook auf einem PC oder Mac genutzt werden. Um eine Raspberry Pi Kamera auf dem Raspberry Pi zu starten, müssen Sie den Befehl `libcamera-vid -n -t 0 --width 1280 --height 960 --framerate 1 --inline --listen -o tcp://127.0.0.1:8888` im Terminal ausführen. 

Um den Python-Code auszuführen, stellen Sie sicher, dass das YOLOv8-Modell heruntergeladen und im richtigen Pfad platziert ist. Bevor Sie den Code ausführen, sollten Sie überprüfen, dass alle Abhängigkeiten installiert sind.

