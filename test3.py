import cv2
import pytesseract
import string

def extract_special_characters(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply image preprocessing
    # preprocessed_image = cv2.medianBlur(gray_image, 3)
    # preprocessed_image = cv2.threshold(preprocessed_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # preprocessed_image = cv2.GaussianBlur(preprocessed_image, (5, 5), 0)

    # Perform OCR using pytesseract
    extracted_text = pytesseract.image_to_string(gray_image)

    # Filter out non-special characters
    # special_characters = ''.join([char for char in extracted_text if char in string.punctuation])

    return extracted_text

def save_text_to_file(text, file_path):
    with open(file_path, 'a') as file:
        file.write(text + '\n')

# Specify the image file path
image_path = 'abc.jpg'

# Specify the text file path
text_file_path = 'special_characters.txt'

# Extract special characters from the image
special_chars = extract_special_characters(image_path)

# Save the extracted special characters to the text file in append mode
save_text_to_file(special_chars, text_file_path)
