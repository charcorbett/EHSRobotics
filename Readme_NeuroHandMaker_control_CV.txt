README for Arduino and Python Code for Controlling Servos of NeuroMaker Hand with Hand Gestures
Overview
This README provides instructions and details about the Arduino and Python code that allows you to control five servo motors of NuroMaker Hand using hand gestures captured by a webcam.

Dependencies
Arduino Code
Arduino IDE
Servo Library
Python Code
OpenCV
cvzone
pySerial
Arduino Code
arduino_servo_control.ino
Overview
This Arduino code is responsible for controlling five servo motors based on the input received from the Python code via the serial connection.

Instructions
Install the Arduino IDE and open the arduino_servo_control.ino file.
Ensure that you have the Servo library installed.
Connect your Arduino to the computer.
Select the correct Arduino board and port in the Arduino IDE.
Upload the code to the Arduino board.
Code Explanation
The code uses the Servo library to control five servos connected to pins 2 through 6.
It listens for a string of commands via the serial connection.
Each command is a string with five binary values (0 or 1), representing the state of each servo.
The code reads and interprets the incoming data and adjusts the servo positions accordingly.
Python Code
hand_gesture_control.py
Overview
This Python code captures hand gestures from a webcam using OpenCV and the cvzone library. It sends the detected finger states to the Arduino via a serial connection to control the servos.

Instructions
Install the required Python libraries using pip:

bash
Copy code
pip install opencv-python cvzone pyserial
Connect your Arduino to your computer via a USB cable.

Update the COM7 in mySerial = SerialObject("COM7", 9600, 1) to the appropriate COM port your Arduino is connected to.

Run the Python script hand_gesture_control.py.

A webcam window will open, and it will start detecting hand gestures.

Make hand gestures to control the servos. For example, show an open palm or close your fingers to trigger servo movements.

Code Explanation
The code captures video from the default camera and uses the cvzone library to detect and track hand landmarks.

It sends the state of the fingers (0 or 1) to the Arduino via a serial connection.

The Arduino processes the received finger states and moves the servos accordingly.

Using the System
Start the Arduino code by uploading it to your Arduino board.

Run the Python script on your computer.

A live webcam feed will open, and it will start detecting your hand.

Control the servos by making different hand gestures. For example, open or close your fingers to move the servos.

Observe the servos responding to your gestures.

Troubleshooting
Ensure that you have the correct COM port for the Arduino in the Python code.

Make sure the servos are connected to the correct pins on the Arduino.

Check the baud rate settings in both the Arduino and Python code.

Ensure that the Arduino is correctly powered and connected to your computer.

Additional Notes
Feel free to customize the gestures and servo movements according to your requirements by modifying the code.

You can experiment with different hand gestures to trigger various servo positions.

Be cautious while working with servo motors to avoid any physical harm or damage to objects in the servo's path.

To exit the Python script, press Esc or close the webcam window.

