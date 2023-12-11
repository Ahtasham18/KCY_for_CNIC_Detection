import cv2 as cv
import mediapipe as mp
from Image_Processing import *

# detect face from image (to recognize id card)
def detect_faces(image):
    # Initialize MediaPipe Face Detection
    mp_face_detection = mp.solutions.face_detection
    face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.3)

    height, width, _ = image.shape

    # Convert the image to RGB
    rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    # Perform face detection
    result = face_detection.process(image)

    # Draw bounding boxes around detected faces
    if result.detections:
        for detection in result.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = image.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            cv.rectangle(image, (x, y-90), (x + w, y + h+40), (0, 255, 0), 2)
    
            return image