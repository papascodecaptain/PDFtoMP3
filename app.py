# Import necessary modules
from PyPDF2 import PdfReader  # For reading PDF files
import pyttsx3  # For converting text to speech
from gtts import gTTS  # For creating the speech output

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    # Create a PdfReader object to read the PDF file
    reader = PdfReader(pdf_path)
    
    # Initialize an empty string to store the extracted text
    text = ""
    
    # Loop through each page in the PDF
    for page in reader.pages:
        # Extract the text from the page and append it to the 'text' variable
        text += page.extract_text()
    
    # Return the accumulated text
    return text

# Function to convert text to speech and save as an audio file
def convert_text_to_speech(text, output_file):
    # Create a gTTS (Google Text-to-Speech) object using the input text
    tts = gTTS(text)
    
    # Save the speech as an audio file with the specified output file name
    tts.save(output_file)

# Path of the PDF file to be processed
pdf_path = "es.pdf"

# Extract all the text from the PDF file
all_text = extract_text_from_pdf(pdf_path)

# Name of the output audio file
output_file = "output.mp3"

# Convert the extracted text to speech and save it as an audio file
convert_text_to_speech(all_text, output_file)
