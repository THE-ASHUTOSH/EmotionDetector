# Emotion Detection with OpenCV and FER  

## 📖 Overview  
This project is an emotion detection application that captures images using a webcam and analyzes the detected facial emotions in real-time. The program leverages OpenCV for image capture and the FER (Facial Expression Recognition) library to detect and analyze emotions such as happiness, sadness, anger, and more. Based on the detected emotion, a personalized motivational or thoughtful message is displayed.  

---

## 🛠 Libraries and Tools Used  
- **OpenCV**: For accessing the webcam and handling image processing tasks.  
- **FER**: A library for facial expression recognition.  
- **TensorFlow**: Underlying dependency for the FER library.  
- **MoviePy**: A FER dependency to manage multimedia files.  

---

## 🚀 Challenges Faced and Solutions  

### 1. Low Emotion Detection Accuracy  
- **Problem**: The program sometimes failed to detect emotions accurately under poor lighting.  
- **Solution**: To address this, better lighting conditions were ensured during testing.  

### 2. Real-Time User Interaction  
- **Problem**: Program sometimes failed to detect correct emotion in real time under poor lighting condition .  
- **Solution**: Added a method a click a particular frame and analyze the it. If the emotion was not found, then prompted the user to retake the image.

### 3. Libraries not supported in the latest version of python
- **Problem**: Many libraries were not supported in the latest version of the python.
- **Solution**: Rolled down to the previous versions.

---

## 💻 Instructions to Run the Code  

### Prerequisites  
Ensure you have Python 3.8 to 3.11 installed on your system.  

### Installation  
1. Clone the repository or download the source code.  
2. Navigate to the project directory.
   
      ```bash
      cd EmotionDetector
      
3. Set up a Python virtual environment (optional but recommended)
   
   - Create a virtual environment:
     
      ```bash
      python -m venv venv
      
   - Activate the virtual environment:
     - On Windows:
       
          ```bash
          venv\Scripts\activate
          
      - On macOS/Linux:
        
           ```bash
           source venv/bin/activate
           
4. Install the required dependencies by running:
   
   ```bash
   pip install -r requirements.txt

### Run the code
1. Run the code using:
   
   ```bash
   python emotion_detector.py

2. A VideoCapture(camera screen) screen would have opened. (If not visible, search for it the taskbar or else a message would be shown in the console.)
   
3. Follow the instructions displayed in the terminal:
- Press 's' to capture an image and detect emotion.
- Press 'r' to retake the picture.
- Press 'q' to quit the application.

---

## 🔖 Note

### For best results, use the application in a well-lit environment.

### Check for the python version before running the app.

- ⭐ The code can be modified for real time emotion detection with some basic changes, but due to inaccurate emotion detection in low light condition it would show variable results, which is not useful.
