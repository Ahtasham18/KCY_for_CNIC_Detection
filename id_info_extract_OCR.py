import cv2
import pytesseract
import re

# Set the path to the Tesseract executable 
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
# extract text from image using OCR
def extract_text_from_image(image_path):
    # Read the image
    img = cv2.imread(image_path)
    cv2.imshow('region of interest',img)
    cv2.waitKey(0)
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # Use pytesseract to extract text
    text = pytesseract.image_to_string(gray, config='--psm 6')  # '--psm 6' assumes a sparse text with uniform font

    return text


#filter cnic_dob_issue_expiry  (new id card)
def extract_cnic_dob_issue_expiry(text):
    # Define a regular expression pattern for numeric strings with hyphens and dots
    numeric_string_pattern = re.compile(r'\b\d+[-.,\d]*\b')

    # Find all matches in the text using the regular expression
    numeric_string_matches = numeric_string_pattern.findall(text)

    # Extract the first four numeric strings (assuming their order in the text)
    cnic_no = numeric_string_matches[0] if len(numeric_string_matches) > 0 else None
    dob = numeric_string_matches[1] if len(numeric_string_matches) > 1 else None
    date_of_issue = numeric_string_matches[2] if len(numeric_string_matches) > 2 else None
    date_of_expiry = numeric_string_matches[3] if len(numeric_string_matches) > 3 else None

    return cnic_no, dob, date_of_issue, date_of_expiry

# filter Name_Gender
def extract_Name_Gender(text):
    # Ensure text is a string (extracting the first element if it's a tuple)
    text = text[0] if isinstance(text, tuple) else text

    # Define regular expressions for names, gender, and country names
    name_pattern = re.compile(r'\b([A-Za-z]+)\b')
    gender_pattern = re.compile(r'\b(M|F)\b', flags=re.IGNORECASE)
    

    # Initialize variables to store extracted information
    names = []
    genders = []
    
    # Find matches in the text using regular expressions
    name_matches = name_pattern.findall(text)
    gender_matches = gender_pattern.findall(text)
    
    
    # Store the extracted information in their respective lists
    names.extend(name_matches)
    genders.extend(gender_matches)
    
    #raw text
    black_text=['Name','Father','Father Name','eltict','Muhai','fatherName','M','Pakitan','ee','SS','wily','CountryofStay','Gender','M_} Pakist','Pakistan']
    names_list = [value for value in names if value not in black_text]
       
    
    return names_list,genders


# filter cnic_and_dob (old card)
def extract_cnic_and_dob(text):
    # Define a regular expression pattern for CNIC-like strings
    cnic_pattern = re.compile(r'\b\d{5}-\d{7}-\d\b')

    # Define a regular expression pattern for date-like strings
    dob_pattern = re.compile(r'\b\d{2}/\d{2}/\d{4}\b')

    # Find all matches in the text using the regular expressions
    cnic_matches = cnic_pattern.findall(text)
    dob_matches = dob_pattern.findall(text)

    # Extract the first CNIC number (if available) and the first date of birth (if available)
    cnic = cnic_matches[0] if cnic_matches else None
    dob = dob_matches[0] if dob_matches else None

    return cnic, dob



