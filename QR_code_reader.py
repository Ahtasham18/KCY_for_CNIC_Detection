import cv2
from yolov8 import YOLOv8
from pyzbar.pyzbar import decode

# decode QR code for getting cnic number
def qr_code_detector(img_path):
    cnic_back_number = None


    model_path = "model/best.onnx"
    yolov8_detector = YOLOv8(model_path, conf_thres=0.2, iou_thres=0.3)
 
    img = cv2.imread(img_path)

    # Detect Objects
    boxes, scores, class_ids = yolov8_detector(img)

    # detect QR code image
    yolov8_detector.draw_detections(img)

    # Convert the image to grayscale (required for QR code detection)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # decode QR codes
    qr_codes = decode(gray_img)
     
    # check QR code 
    if qr_codes:
            # Extract and print the QR code data
            for qr_code in qr_codes:
                
                cnic_back_number = qr_code.data.decode('utf-8')
                return cnic_back_number[12:25]
        
    else:
        return False

