from flask import Flask, Response
import cv2

app = Flask(__name__)

# OpenCV capture from the Raspberry Pi camera (or USB camera)
camera = cv2.VideoCapture(0)  # 0 for default camera, adjust if needed

# Function to generate frames from the camera
def generate_frames():
    while True:
        success, frame = camera.read()  # Read a frame from the camera
        if not success:
            break
        else:
            # Encode the frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Use yield to stream the frame in a multipart format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Route to serve the video stream
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route to serve the HTML page that displays the video stream
@app.route('/')
def index():
    return '''
        <html>
            <head>
                <title>Live Video Stream</title>
            </head>
            <body>
                <h1>Live Video Feed</h1>
                <img src="/video_feed" style="width:640px; height:480px;">
            </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
