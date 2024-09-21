# **Raspberry Pi Video Streaming with Flask and OpenCV**

This project demonstrates how to stream video from a Raspberry Pi's camera or USB camera using **OpenCV** and **Flask**. The live video feed is captured using OpenCV and streamed over a local network to any device connected to the same network. The video is served through a simple web interface, making it accessible via a web browser.

## **Features**
- Live video streaming from the Raspberry Pi's camera.
- Web interface accessible from any device connected to the same network.
- Lightweight and easy to deploy on any Raspberry Pi.

## **Requirements**

- **Raspberry Pi** (tested on Raspberry Pi 4/5, but should work on earlier models)
- **Raspberry Pi Camera** or **USB camera**
- **Python 3**
- **Flask** and **OpenCV**

### **Python Dependencies**
- Flask (`2.3.2`)
- OpenCV (`4.8.0.74`)

You can find these in the `requirements.txt` file for easy installation.

⚠️ Warning: While im confident this will work for most use cases, mileage will vary based on certain hardware restrictions 

## **Installation Instructions**

### **1. Setting Up the Raspberry Pi**

Make sure your Raspberry Pi is set up and that the camera is enabled.

1. Update your system:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

   ⚠️ Warning: The below step is not required or even possible in rpi5 with bookworm. 
2. Enable the Raspberry Pi camera (if using the Raspberry Pi Camera Module):
   ```bash
   sudo raspi-config
   ```
   Go to **Interfacing Options** > **Camera** and enable it. Then reboot the Pi:
   ```bash
   sudo reboot
   ```

### **2. Clone the Project**

Clone the repository (or create the necessary files if not using version control):
```bash
git clone (https://github.com/CanonEllis/rpi_video.git)
cd <project-folder>
```

### **3. Install Dependencies**
⚠️ **Warning:** This project will most likely need to be done in venv, if you are unsure how to do that, reach out to me at my school email. 

First, make sure you have `pip` installed. Then install the dependencies listed in the `requirements.txt` file:
```bash
pip3 install -r requirements.txt
```

This command installs Flask and OpenCV, which are required for the application.

### **4. Running the Application**

To start the Flask application that streams video:

1. Run the Flask app:
   ```bash
   python3 app.py
   ```

   This will start the Flask server on the Raspberry Pi, listening on port `5000`.

2. On any device connected to the same local network, open a browser and navigate to the Raspberry Pi's IP address:
   ```
   http://<raspberry-pi-ip>:5000
   ```

   For example:
   ```
   http://192.168.1.100:5000
   ```

   You will now see the live video stream from the Raspberry Pi camera.

## **File Structure**

```
├── app.py                   # Main Python script that runs the Flask server and streams video.
├── requirements.txt          # Python dependencies needed for the project.
└── README.md                 # Documentation for the project.
```

### **app.py**:

```python
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
```

### **requirements.txt**:
This file lists all the dependencies required to run the application:
```
Flask==2.3.2
opencv-python==4.8.0.74
```

## **Accessing the Video Stream**

1. Make sure the Raspberry Pi and the device you are accessing it from (e.g., a laptop or phone) are on the same local network (Wi-Fi or Ethernet).
2. Open a browser and go to `http://<raspberry-pi-ip>:5000`.
3. The video feed should be visible.

## **Troubleshooting**

- **Camera Not Found**: Ensure that the camera is enabled via `raspi-config`, and that it is correctly connected.
- **Wrong IP Address**: Use `hostname -I` on the Raspberry Pi to find its IP address on the network.
- **Camera Capture Issues**: If using a USB camera, you may need to adjust the `cv2.VideoCapture()` index (`0`, `1`, etc.) depending on which camera is being used.

## **License**

This project is licensed under the MIT License.
