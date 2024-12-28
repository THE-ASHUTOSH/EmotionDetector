import cv2
from fer import FER
import logging

detector = FER()

emotion_messages = {
    "happy": "Your smile lights up the room!",
    "neutral": "Your presence is calm and confident!",
    "sad": "You’ve got this, keep going!",
    "angry": "Take a deep breath; you're stronger than your anger.",
    "surprise": "Wow, you seem pleasantly surprised!",
    "disgust": "Let’s turn that frown upside down!",
    "fear": "It’s okay to feel scared. You’re brave!"
}

def capture_picture_with_emotion(output_filename="captured_image.jpg"):
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Error: Could not access the webcam.")
        return

    print("Press 's' to capture an image, and detect emotion, 'r' to retake or 'q' to quit.")

    while True:
        ret, frame = cam.read()

        if not ret:
            print("Error: Unable to capture video.")
            break

        cv2.imshow("Webcam - Press 's' to capture", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):

            emotion, score = detector.top_emotion(frame)

        
            
            if emotion and score:
                message = emotion_messages.get(emotion)
                print(f"Detected Emotion: {emotion} with confidence {score*100:.2f}%")
                cv2.putText(frame, f'Emotion: {emotion} ({score*100:.2f}%)', (50, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(frame, message, (50, 100), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.imshow("Captured Image with Emotion", frame)
                cv2.waitKey(0)  
                break
            else:
                print("No emotion detected.")
                cv2.putText(frame, 'No emotion detected', (50, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                cv2.putText(frame, 'Press R to retake', (50, 100), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow("Captured Image with Emotion", frame)
                

            
        elif key == ord('r'):
            print("Restarting...")
            cv2.destroyAllWindows()
            cam.release()
            capture_picture_with_emotion()
            break

        elif key == ord('q'):
            print("Exiting without saving.")
            break

    cam.release()
    cv2.destroyAllWindows()

capture_picture_with_emotion()

