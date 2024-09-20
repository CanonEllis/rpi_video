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

## **Installation Instructions**

### **1. Setting Up the Raspberry Pi**

Make sure your Raspberry Pi is set up and that the camera is enabled.

1. Update your system:
   ```bash
   sudo apt update && sudo apt upgrade -y
