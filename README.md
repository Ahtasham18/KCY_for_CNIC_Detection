# KCY_for_CNIC_Detection
This Project help to detect National ID card and Store ID information with the help of OCR which more useful for organisation and  different Projects.

1. Firstly project read back and front card image.
2. Detect card image through custom trained yolo model.
3. After detection, detected part/card crop and split into two parts(right or left) for id card classification(old or new id card).
4. In classification send right and left image to detect face in the image and classify them.
5. After classification: old card image send to OCR that extract information and store in csv file but in case of new id card, image preprocess and crop roi and pass to OCR then extract information
6. After that back id card image pass qr_reader.py and return cnic no then identify front and back cnic number of id card if valid then new id card data store in csv file.  
