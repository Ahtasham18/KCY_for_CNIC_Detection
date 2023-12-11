import pandas as pd

# store data in CSV file (new id Card)
def save_id_data_new(names,gender,cnic,dob,doi,doe):

    name=' '.join(names)
# Combine the information into a dictionary
    data = {
        "Name & Father Name": [name],
        "Gender":[gender],
        "CNIC": [cnic],
        "Date of Birth": [dob],
        "Date of Issue": [doi],
        "Date of Expiry": [doe]
    }

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)

    # Define the CSV file path
    csv_file_path = "id_data_new.csv"

    # Check if the CSV file already exists
    try:
        existing_data = pd.read_csv(csv_file_path)

        # Append the new data to the existing DataFrame
        df = pd.concat([df], ignore_index=True)
    except FileNotFoundError:
        # If the file doesn't exist, create a new CSV file
        df.to_csv(csv_file_path, index=False)

    # Append the new data to the CSV file
    df.to_csv(csv_file_path, mode='a', header=False, index=False)

# store data in CSV file (old id Card)
def save_id_data_old(cnic,dob):
# Combine the information into a dictionary
    data = {
       
        "CNIC": [cnic],
        "Date of Birth": [dob],
    }

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)

    # Define the CSV file path
    csv_file_path = "id_data_old.csv"

    # Check if the CSV file already exists
    try:
        existing_data = pd.read_csv(csv_file_path)

        # Append the new data to the existing DataFrame
        df = pd.concat([df], ignore_index=True)
    except FileNotFoundError:
        # If the file doesn't exist, create a new CSV file
        df.to_csv(csv_file_path, index=False)

    # Append the new data to the CSV file
    df.to_csv(csv_file_path, mode='a', header=False, index=False)

