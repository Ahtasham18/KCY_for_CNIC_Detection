# import libraries
from Card_Detector import *
from Image_Processing import *
from Face_detection import *
from QR_code_reader import *
from id_info_extract_OCR import *
from ID_data_store import *
import cv2 as cv


# main body
if __name__=="__main__":
    
    # front of new id card
    front_path='test_img/mf.png'
    
    # front of old id card
    # front_path='test_img/o2.jpg'
    
    back_path='test_img/mb.png'
    
    # call enhance_image_quality func and get improve image  
    enhance_image=enhance_image_quality(front_path)
    
    # read enhance_image 
    front_image=cv.imread(enhance_image)
    cv.imshow("Enhanced image", front_image)
    cv.waitKey(0)
    
    # detection of image (is a card or not)
    detection,crop_img=detection_card(front_image)
    
    
   
    # check condition is card or not
    if detection==True and crop_img is not None:
        print('##############################################################################\n\n')
        print('Hurre! Card detected.\n')
        print('##############################################################################\n\n')
        left_image, right_image = divide_image(crop_img)
        
        cv.imshow('Left Image', left_image)
        cv.imshow('Right Image', right_image)
        cv.waitKey(0)
    else:
        print('##############################################################################\n\n')
        print('Sorry card is not detected! kindly upload card image or upload the clear image. Remember this program is detect for only Pakistani ID card.Thanks\n')
        print('##############################################################################\n\n')
        exit()
     
     # Classification of a id card    
    left_face=detect_faces(left_image)
    right_face=detect_faces(right_image)
    
    # classify old id card
    if left_face is not None:
        print('##############################################################################\n\n')
        print('Identified! its old pakistani national identity card\n')
        print('##############################################################################\n\n')
        cv2.imshow("National ID Card(OLD)",crop_img)
        cv.waitKey(0)
        
        # resized crop image
        resize_image()
        
         # 1 Extract information from the image(upper info)
        input_image_path = 'output/cropped_card.jpg' 
        extracted_text = extract_text_from_image(input_image_path)
        
        # Print the extracted text
        print('##############################################################################\n\n')
        print(f"Extracted Text: {extracted_text}")
        print('##############################################################################\n\n')
            
        # Extract the CNIC number and date of birth from the text
        cnic, dob = extract_cnic_and_dob(extracted_text)
        
        

        # Display  the extracted information
        print("CNIC No:", cnic)
        print("Date of Birth:", dob)
        print('##############################################################################\n\n')
        
        # to store extracted data
        save_id_data_old(cnic,dob)

    # clasify new id card
    elif right_face is not None:
        print('##############################################################################\n\n')
        print('Identified! its new pakistani national identity card\n')
        print('##############################################################################\n\n')
        cv2.imshow("National ID Card(New)",crop_img)
        cv.waitKey(0)
        
        # resized crop image
        resize_image()
        
        # extract data from id card
        path='output/resized_image.jpg'
        crop_information_new(path)
        
        # 1 Extract information from the image(upper info)
        input_image_path = 'output/upper_info.jpg' 
        extracted_text = extract_text_from_image(input_image_path)
        
        # Print the extracted text
        print('##############################################################################\n\n')
        print(f"Extracted Text: {extracted_text}")
        print('##############################################################################\n\n')

        # Extract useful information from the filtered text
        names,genders= extract_Name_Gender(extracted_text)
        

        # 2 Extract information from the image(lower info)
        input_image_path = 'output/lower_info.jpg' 
        extracted_text = extract_text_from_image(input_image_path)
        
        # Print the extracted text
        print('##############################################################################\n\n')
        print(f"Extracted Text: {extracted_text}")
        print('##############################################################################\n\n')

        # Extract and store numeric strings into categories
        cnic_no, dob, date_of_issue, date_of_expiry = extract_cnic_dob_issue_expiry(extracted_text)
        
        
       
        
        # for identify! check back CNIC number using QR reader to ectract CNIC number
        cnic_no_back=qr_code_detector(back_path)  
        print("CNIC Number(Back Side): ",cnic_no_back)
        print('\n##############################################################################\n\n')
        
        if cnic_no is not None:
            cnic_no=cnic_no.replace('-','')
        else:
            print("CNIC number is not extract accurately! kindly upload high quality card image. Thank you")
            exit()
         # print('CNIC G:',cnic_no)
        if  cnic_no!=cnic_no_back:
            print("Verified! Front and Back of ID Card is Same ")
            print('\n##############################################################################\n\n')
            
            # # Display  the extracted information
            print("Name & Father Name:", ' '.join(names))
            print("Gender:",genders)
            print("CNIC No:", cnic_no)
            print("Date of Birth:", dob)
            print("Date of Issue:", date_of_issue)
            print("Date of Expiry:", date_of_expiry)
            
            # to store extracted data
            save_id_data_new(names,genders,cnic_no,dob,date_of_issue,date_of_expiry)
            print('##############################################################################\n\n')
            
        else:
            print("Oops! Front and Back of ID Card is not same. kindly upload same id card front and back image ")
            print('##############################################################################\n\n')
            # Display  the extracted information
            print("Name & Father Name:", ' '.join(names))
            print("Gender:",genders)
            print("CNIC No:", cnic_no)
            print("Date of Birth:", dob)
            print("Date of Issue:", date_of_issue)
            print("Date of Expiry:", date_of_expiry)
            exit()
            
    else:
        print('##############################################################################\n\n')
        print('Not identify Pakistani National ID card! so upload national ID card. Thanks\n')
        print('##############################################################################\n\n')
        exit()
        
