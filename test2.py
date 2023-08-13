import cv2
import pytesseract
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def extract_text_from_image(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply image preprocessing
    # preprocessed_image = cv2.medianBlur(gray_image, 3)
    # preprocessed_image = cv2.threshold(preprocessed_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # preprocessed_image = cv2.GaussianBlur(preprocessed_image, (5, 5), 0)

    # Perform OCR using pytesseract
    # extracted_text = pytesseract.image_to_string(preprocessed_image)
    # custom_config = r'--psm 6 -c preserve_interword_spaces=1'
    extracted_text = pytesseract.image_to_string(gray_image)

    # cv2.imshow('Result', preprocessed_image)
    # cv2.imshow('Result', gray_image)
    # cv2.waitKey(0)

    return extracted_text

def save_text_to_file(text, file_path):
    with open(file_path, 'a') as file:
        file.write(text + '\n')

# Create a Tkinter root window
root = Tk()
root.withdraw()  # Hide the root window

# Prompt the user to select an image file using the file dialog
image_path = askopenfilename(title="Select an image file", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

if image_path:
    # Specify the image file path
    # Specify the text file path
    text_file_path = 'extracted_text.txt'

    # Extract text from the image
    extracted_text = extract_text_from_image(image_path)

    # Save the extracted text to the text file in append mode
    save_text_to_file(extracted_text, text_file_path)
else:
    print("no path")