#the purpose of this script is to detect the charset of the csv file provided since it was raising errors.
import chardet

def detect_csv_encoding(file_path):
    with open(file_path, 'rb') as raw_file:
        result = chardet.detect(raw_file.read())
    return result['encoding']

csv_file_path = "upload/gamerounds.csv"  # Adjust the path to your CSV file
csv_encoding = detect_csv_encoding(csv_file_path)
print(f"Detected CSV Encoding: {csv_encoding}")
