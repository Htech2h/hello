import cv2
import torch
from facenet_pytorch import MTCNN

# Initialize MTCNN
mtcnn = MTCNN()

# Open video file
video_path = "calcuAi/WhatsApp Video 2023-08-23 at 16.31.01.mp4" 
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detect faces using MTCNN
    boxes, _ = mtcnn.detect(rgb_frame)
    
    if boxes is not None:
        for box in boxes:
            x, y, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x, y), (x2, y2), (0, 255, 0), 2)

    # Display the frame with bounding boxes
    cv2.imshow('Face Detection', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()


