#import libraries
import cv2 as cv
import mediapipe as mp
from PIL import Image
import os

# improve the quality of image
def enhance_image_quality(image_path,resize_factor=1.5, denoise_kernel_size=(5, 5), contrast_alpha=1.2, contrast_beta=10):
    
    # read image
    img = cv.imread(image_path)

    # Convert the image to grayscale
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Denoise the image
    denoised_img = cv.fastNlMeansDenoising(gray_img, None, h=denoise_kernel_size[0], templateWindowSize=denoise_kernel_size[1], searchWindowSize=denoise_kernel_size[1])

    # Adjust contrast
    enhanced_img = cv.convertScaleAbs(denoised_img, alpha=contrast_alpha, beta=contrast_beta)

    # Save the enhanced image
    output_path='/Users/ahtashamulhaq/ONNX-YOLOv8-Object-Detection-main/output/enhanced.jpg'
    cv.imwrite(output_path, enhanced_img)
    return output_path




# divide image into two parts(left and right) 
def divide_image(image):

    # Get the width and height of the image
    height, width, _ = image.shape

    # Calculate the midpoint of the width
    mid_point = width // 2

    # Divide the image into left and right parts
    left_image = image[:, :mid_point, :]
    right_image = image[:, mid_point:, :]
    
    return left_image, right_image

# resized image
def resize_image():
    # Open the image and resize it to the target size 
    img_resized = Image.open('output/cropped_card.jpg').resize((500, 450))

    # Save the resized image
    img_resized.save("output/resized_image.jpg")

# image crop for data extraction (new card)
def crop_information_new(image_path):
    
    
    #read image
    image=cv.imread(image_path)
    
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
            # cv.rectangle(image, (x, y-50), (x + w, y + h+45), (0, 255, 0), 2)
              # Draw rectangle to the left of the detected face
            # left_rect_length = 280  # Adjust the length as needed
            
          
            
            left_rect_length = 250 # Adjust the length as needed
            upper_info = (max(0, x - left_rect_length), y-85, x, y + h+50)
            cv.rectangle(image, (max(0, x - left_rect_length), y-85), (x-10, y + h+50), (0, 0, 255), 2)
            
            lower_info = (max(0, x - left_rect_length), y + h+50, x-10, y + h+170)
            cv.rectangle(image, (max(0, x - left_rect_length), y + h+50), (x-10, y + h+170), (255, 0, 0), 2)

            # Crop the upper_info and lower_info rectangles
            x_left_upper, y_upper, x_right_upper, y_bottom_upper = upper_info
            cropped_image_upper = image[y_upper:y_bottom_upper, x_left_upper:x_right_upper]

            x_left_lower, y_lower, x_right_lower, y_bottom_lower = lower_info
            cropped_image_lower = image[y_lower:y_bottom_lower, x_left_lower:x_right_lower]

            # Save the cropped images
            output_path_upper = os.path.join('output/upper_info.jpg')
            output_path_lower = os.path.join('output/lower_info.jpg')
            cv.imwrite(output_path_upper, cropped_image_upper)
            cv.imwrite(output_path_lower, cropped_image_lower)
        
        


