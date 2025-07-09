# HydroSenseAI
Hybrid Drown Detection System using Computer Vision and Simulated Sensors

## Inspiration:
Drowning is one of the leading causes of accidental deaths, particularly among children. I remember when I was younger, I often wanted to go swimming, but I always needed my parents to supervise me. Sometimes they were too busy, and my plans to go to the pool had to be cancelled. Other times, I saw kids who went swimming without any supervision, putting themselves at serious risk. These memories made me think about how easily such accidents can happen and how technology could play a role in preventing them. This inspired me to develop a hybrid drowning detection system that combines AI-powered computer vision with simulated sensor data to detect early signs of distress in swimmers. My goal with this project is to create a tool that can assist lifeguards, or even operate autonomously to monitor swimmers and to prevent drowning accidents, especially for children like I once was.

## Description:
HydroSenseAI is a hybrid drowning detection system designed to enhance swimmer safety through AI-powered computer vision and simulated sensor data. This project explores how technology can assist in preventing drowning incidents by combining pose detection and sensor simulation. 

## Features:
- Pose Detection powered by AI using MediaPipe Pose Estimation
- Motion tracking to detect abnormal or dangerous swimming behaviour which could potentially lead to drowning
- Simulated pressure sensor readings for hybrid drowning detection
- Real-time alerts when drowning risk is detected

## Technologies Used:
- Python
- OpenCV
- MediaPipe Pose (AI Pose Estimation Model)
- Simulated Sensor Data
- Playsound (for alert sounds)

## Operating Mechanism:
The system works by detecting and tracking key body points from video footage or a webcam to monitor swimmers’ movements. It observes specific landmarks, such as the nose, to estimate how long someone has been submerged underwater. Alongside this, it simulates data from pressure or motion sensors that could identify if a swimmer has remained still underwater for too long. By combining these two sources of information—camera footage and sensor readings—the system can trigger alerts when it detects potential drowning situations.

## Future Plans:
In the future, I plan to develop this project beyond the laptop prototype by using a Jetson Nano, a compact and powerful device designed for running processing tasks locally. This would enable the system to operate independently, continuously analyzing video and sensor data in real time without relying on a laptop. I intend to connect external sensors such as pressure, depth, or motion sensors along with cameras to the Jetson Nano to enhance detection accuracy and reliability, including in more challenging environments like outdoor pools. To support this, I will adjust the existing code to run efficiently on the Jetson Nano, focusing on optimizing performance and integrating sensor data smoothly. I also plan to improve the computer vision component by developing models specifically tailored for underwater conditions to increase detection accuracy. Additionally, I aim to build a web or mobile dashboard to provide live monitoring and real-time alerts, making the system more accessible and user-friendly. Finally, I plan to explore training custom models based on collected data to further improve the system’s reliability. To enhance safety measures, I will develop a separate connected device capable of automatically contacting emergency services, such as dialing 911, if a high-risk drowning situation is detected. This would ensure prompt external assistance even when no lifeguards or supervisors are present.

## Author
Developed by Aryan Srujan Chinthamreddy (Personal Project)



