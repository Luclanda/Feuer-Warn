from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime, timedelta
from ultralytics import YOLO
import threading

class MyServer(BaseHTTPRequestHandler):
    detected_feuer = []

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<!DOCTYPE html>", "utf-8"))
        self.wfile.write(bytes("<html>", "utf-8"))
        self.wfile.write(bytes("<head>", "utf-8"))
        self.wfile.write(bytes("<title>Feuer-Warn</title>", "utf-8"))
        self.wfile.write(bytes("</head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))

        self.wfile.write(bytes("<h2>Feuer gefunden:</h2>", "utf-8"))
        for feuer_info in self.detected_feuer:
            self.wfile.write(bytes("<p>%s</p>" % feuer_info, "utf-8"))

        self.wfile.write(bytes("</body></html>", "utf-8"))

def run_web_server():
    server_address = ('192.168.178.80', 8080)
   # server_address = ('127.0.0.1', 5875)
    webServer = HTTPServer(server_address, MyServer)
    print("Server started at http://%s:%s" % server_address)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

def run_go():
    model = YOLO('/Users/lucalandsiedel/Downloads/feuer-3.pt')
    results = model(stream=True, source=0, show=True, conf=0.5, verbose=False)
#    results = model("tcp://192.168.178.134:8888", stream=True, show=True, conf=0.5, verbose=False)
    
    try:
        while True:
            for result in results:
                for box in result.boxes:
                    if box.cls == 80.00:
                        if box.conf > 0.8:
                            c = datetime.now()
                            current_time = c.strftime('%H:%M:%S')
                            feuer_info = 'Feuer gefunden um %s mit der confidence %f' % (current_time, box.conf*100)

                        MyServer.detected_feuer.append(feuer_info)
                    
    except KeyboardInterrupt:
        print("Beendet.")

if __name__ == "__main__":
    import threading
    web_server_thread = threading.Thread(target=run_web_server)
    web_server_thread.start()

    run_go()
