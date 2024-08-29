# Attendence-system-ML
 
## Overview

This project implements an advanced smart attendance system using facial recognition technology, powered by YOLOv7 for face detection. Built with Python, it automates the process of marking attendance by recognizing faces in real-time through a camera feed, leveraging the speed and accuracy of YOLOv7.

## Features

- Real-time face detection using YOLOv7
- Facial recognition for identity verification
- Automated attendance marking
- User-friendly GUI for easy interaction
- Attendance reports generation
- Database integration for storing student information and attendance records

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- PyTorch
- OpenCV
- YOLOv7
- face_recognition
- numpy
- pandas
- SQLite (or your preferred database system)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Akshat93463/Attendence-system-ML.git
   ```

2. Navigate to the project directory:
   ```
   cd Attendence-system-ML
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Download YOLOv7 weights:
   ```
   wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt
   ```

## Usage

1. Run the main script:
   ```
   python main.py
   ```

2. Use the GUI to navigate through different options:
   - Register new students
   - Start attendance session
   - Generate reports

## Configuration

- Adjust the `config.py` file to modify settings such as:
  - Camera source
  - Database path
  - YOLOv7 model path
  - Face recognition tolerance
  - YOLOv7 confidence threshold

## How It Works

1. **Face Detection**: YOLOv7 is used to detect faces in the camera feed in real-time.
2. **Face Recognition**: Detected faces are then processed using the face_recognition library to identify individuals.
3. **Attendance Marking**: Recognized individuals are marked present in the database.

## Contributing

Contributions to this project are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - akshatj612@gmail.com

Project Link: [https://github.com/Akshat93463/Attendence-system-ML]
(https://github.com/Akshat93463/Attendence-system-ML)

## Acknowledgements

- [YOLOv7](https://github.com/WongKinYiu/yolov7)
- [OpenCV](https://opencv.org/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [PyTorch](https://pytorch.org/)
