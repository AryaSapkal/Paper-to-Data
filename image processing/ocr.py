import pytesseract
from PIL import Image

img = Image.open("sample_text_document.jpg")

text = pytesseract.image_to_string(img)

print(text)