import pytesseract
from PIL import Image
import json
import string

from pythainlp.spell import correct

import os

def ocr_translate(image_path):
  """
  Reads text from a PNG image, translates it to English, and returns the translation.

  Args:
    image_path: Path to the PNG image file.

  Returns:
    The translated text in English, or None if an error occurs.
  """
  try:
    # Open the image
    img = Image.open(image_path)

    # Extract text using Tesseract (specify Thai language)
    text = pytesseract.image_to_string(img, lang='tha')

    return text
  except Exception as e:
    print(f"An error occurred: {e}")
    return None

def remove_punctuation(text):
  """Removes punctuation characters from a string.

  Args:
    text: The string to remove punctuation from.

  Returns:
    The string with punctuation characters removed.
  """

  no_punct = ''.join([char for char in text if char not in string.punctuation])
  return no_punct

# Example usage (replace with your folder path)
image_folder = './data/'

out = {}
f = open("output.json", "a", encoding="utf-8")

for filename in os.listdir(image_folder):
  if filename.endswith('.png'):
    image_path = os.path.join(image_folder, filename)
    translated_text = ocr_translate(image_path)
    if translated_text:
      id = int(filename.split('.')[0])
      translated_text = remove_punctuation(translated_text).strip().replace('\n', '').replace('\t', '').replace(' ', '')
      out[id] = correct(translated_text)
      print(out[id])
    
print(out)

json.dump(out, f)

# data = [[id, translations[id]] for id in translations.keys()]

# data.sort()

# print(data)

# Write the data to a CSV file
# with open('sample.csv', 'w', newline='') as csvfile:
#   writer = csv.writer(csvfile)
#   writer.writerow(['id', 'menu'])  # Write the header row
#   writer.writerows(data)  # Write the data rows

# print("CSV file created successfully: sample.csv")
