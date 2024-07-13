# ImagePatternRecognition

Image Encoding and Decoding Project
This project provides a set of Python scripts to encode text into images and decode text from images. It also includes functions to convert images to base64 strings and vice versa, and to save encoded images as IMR files.

Author
heyanugrah

Creation Date
2024-07-13

Modules and Packages Used
numpy (version 1.21.0 or higher): Used for array manipulation and numerical operations.
base64: Used for encoding and decoding base64 strings.
Pillow (PIL) (version 8.2.0 or higher): Used for image processing tasks.
Ensure you have these packages installed before running the scripts. You can install the required packages using pip:

bash
Copy code
pip install numpy pillow
Functions Overview
read_tranformed_image(image_path)
Reads and decodes text from an encoded image.

Parameters:
image_path (str): Path to the encoded image file.
Returns:
str: Decoded and cleaned string from the image.
decode_text_from_image(image_path)
Decodes text from an image encoded using lines.

Parameters:
image_path (str): Path to the encoded image file.
Returns:
str: Decoded text from the image.
readImr(_imrActualFile, _outputFileUri)
Reads and decodes an image from an encoded IMR file.

Parameters:
_imrActualFile (str): Path to the encoded IMR file.
_outputFileUri (str): Path to save the decoded image.
decode_base64(encoded_string)
Decodes a base64 encoded string to a NumPy array.

Parameters:
encoded_string (str): Base64 encoded string.
Returns:
np.array: Decoded NumPy array.
save_decoded_image(array, output_file)
Saves a decoded NumPy array as an image file.

Parameters:
array (np.array): Decoded NumPy array.
output_file (str): Path to save the decoded image.
load_image_and_save_as_npy(image_path, _outputImrUri)
Loads an image, reshapes it, encodes it to base64, and saves it as an IMR file.

Parameters:
image_path (str): Path to the input image file.
_outputImrUri (str): Path to save the encoded IMR file.
Returns:
bool: True if successful, False otherwise.
encode_to_base64(array)
Encodes a NumPy array to a base64 string.

Parameters:
array (np.array): NumPy array to encode.
Returns:
str: Base64 encoded string.
encode_text_into_image(text, image_path)
Encodes text into an image using lines.

Parameters:
text (str): Text to encode into the image.
image_path (str): Path to save the encoded image.
createImr(_imgUrin, _outputImrUri)
Entry function to read the actual JPEG file and create an IMR file.

Parameters:
_imgUrin (str): Path to the input JPEG file.
_outputImrUri (str): Path to save the encoded IMR file.
Returns:
str: Path to the encoded IMR file if successful, None otherwise.
Usage
Encoding an Image:

python
Copy code
createImr("input_image.jpg", "encoded_image.imr")
Decoding an Image:

python
Copy code
readImr("encoded_image.imr", "decoded_image.jpg")
License
This project is licensed under the MIT License.

This README provides a comprehensive overview of the project, including details about the modules and packages used, and instructions for using the functions provided. Feel free to modify it to suit your needs.
