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
    server_address = ('ip-adress', 5875)
    server_address = ('127.0.0.1', 5875)
    webServer = HTTPServer(server_address, MyServer)
    print("Server started at http://%s:%s" % server_address)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        
        webServer.server_close()
        print("Server stopped.")

def run_go():
    model = YOLO('path/to/the/feuer.pt')
    results = model(stream=True, source=0, show=True, conf=0.5,verbose=False) #this is using your webcame
    results = model("tcp://ip-adress:8888", stream=True, show=True, conf=0.5,verbose=False) #this is using the camera of the raspberry pi
    
    while True:
        for result in results:
            for box in result.boxes:
                if box.cls == 28.00:  
                    if box.conf > 0.5:
                        c = datetime.now()
                        current_time = c.strftime('%H:%M:%S')
                        feuer_info = 'Fire at %s Confidence: %f' % (current_time, box.conf)

                    MyServer.detected_feuer.append(feuer_info)

if __name__ == "__main__":
    web_server_thread = threading.Thread(target=run_web_server)
    web_server_thread.start()

    run_go()
