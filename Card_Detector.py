# import libraries
import cv2
import numpy as np

from ..yolov8 import YOLOv8

# Card detection  using custom train model yolov8
def detection_card(front_img):
    
    # initialize yolov8 object detector and model path
    model_path = "model/best.onnx"
    yolov8_detector = YOLOv8(model_path, conf_thres=0.2, iou_thres=0.3)
    
    # Detect Objects
    boxes, scores, class_ids = yolov8_detector(front_img)
    combined_img = yolov8_detector.draw_detections(front_img)
    cv2.namedWindow("Detected", cv2.WINDOW_NORMAL)
    cv2.imshow("Card", combined_img)
    cv2.waitKey(0)
    print('Boxes',boxes)
    
    # Crop detected region
    if len(boxes) > 0:
        
        # check if any coordinates is negetive if yes then change to positive
        for i, box in enumerate(boxes):
           for j in box:
               if j<0:
                   boxes = np.clip(boxes, a_min=1, a_max=None)
                #    print('kindly upload complete card image with proper corner! thanks\n\n\n')
                #    print('Boxes',boxes)
        # coordinates store in variables to crop id card image from orignal image
        for i, box in enumerate(boxes):
            x, y, w, h = map(int,box)
        cropped_card = front_img[y:h, x:w]
        
        # Display or save the cropped image
        cv2.imshow("Cropped ID Card", cropped_card)
        cv2.imwrite("/Users/ahtashamulhaq/ONNX-YOLOv8-Object-Detection-main/output/cropped_card.jpg", cropped_card)
        # print(cropped_card.shape)
        key = cv2.waitKey(0)
        if key == ord('q') or key == ord('Q'):
            cv2.destroyAllWindows()

        # Return the cropped image
        scores=max(scores)
        if scores*100>=80:
            return True,cropped_card
        else:
            return False,None
    else:
        return False,None
    
    

