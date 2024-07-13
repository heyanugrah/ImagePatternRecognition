"""
Author: heyanugrah
Creation Date: 2024-07-13

This script provides functions to encode text into images and decode text from images.
It also includes functions to convert images to base64 strings and vice versa, and to
save encoded images as IMR files.
"""

import numpy as np
import base64
from PIL import Image, ImageDraw, ImageFont

def read_tranformed_image(image_path):
    """
    Reads and decodes text from an encoded image.

    Parameters:
    image_path (str): Path to the encoded image file.

    Returns:
    str: Decoded and cleaned string from the image.
    """
    # Decode the text from the image
    decoded_text = decode_text_from_image(image_path)
    # Remove any unwanted characters (e.g., '\xff')
    cleaned_string = decoded_text.replace("\xff", "")
    return cleaned_string

def decode_text_from_image(image_path):
    """
    Decodes text from an image encoded using lines.

    Parameters:
    image_path (str): Path to the encoded image file.

    Returns:
    str: Decoded text from the image.
    """
    # Open the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font_size = 0.5
    font = ImageFont.truetype('arial.ttf', font_size)
    width, height = image.size
    line_spacing = 6
    x, y = line_spacing, line_spacing
    decoded_text = ''

    # Iterate over the image pixels to decode the text
    while y < height - line_spacing:
        while x < width - line_spacing:
            color = image.getpixel((x, y))
            red_value = color[0]
            decoded_char = chr(red_value)
            decoded_text += decoded_char
            x += line_spacing + font_size
        x = line_spacing
        y += line_spacing + font_size

    return decoded_text.strip()

def readImr(_imrActualFile, _outputFileUri):
    """
    Reads and decodes an image from an encoded IMR file.

    Parameters:
    _imrActualFile (str): Path to the encoded IMR file.
    _outputFileUri (str): Path to save the decoded image.
    """
    # Read the transformed image to get the cleaned string
    cleaned_string = read_tranformed_image(_imrActualFile)
    # Decode the cleaned string from base64 to a NumPy array
    decoded_array = decode_base64(cleaned_string)
    # Save the decoded NumPy array as an image file
    save_decoded_image(decoded_array, _outputFileUri)

def decode_base64(encoded_string):
    """
    Decodes a base64 encoded string to a NumPy array.

    Parameters:
    encoded_string (str): Base64 encoded string.

    Returns:
    np.array: Decoded NumPy array.
    """
    # Decode the base64 string to bytes
    img_bytes = base64.b64decode(encoded_string)
    # Convert the bytes to an image
    image = Image.frombytes('RGB', (600, 730), img_bytes)
    # Convert the image to a NumPy array
    decoded_array = np.array(image)
    return decoded_array

def save_decoded_image(array, output_file):
    """
    Saves a decoded NumPy array as an image file.

    Parameters:
    array (np.array): Decoded NumPy array.
    output_file (str): Path to save the decoded image.
    """
    # Convert the NumPy array to an image
    image = Image.fromarray(array.astype('uint8'))
    # Save the image
    image.save(output_file)
    print(f"Success!! Decoded image saved as: {output_file}")

def load_image_and_save_as_npy(image_path, _outputImrUri):
    """
    Loads an image, reshapes it, encodes it to base64, and saves it as an IMR file.

    Parameters:
    image_path (str): Path to the input image file.
    _outputImrUri (str): Path to save the encoded IMR file.

    Returns:
    bool: True if successful, False otherwise.
    """
    try:
        # Open the input image
        image = Image.open(image_path)
        # Convert the image to a NumPy array
        image_array = np.array(image)
        # Expected shape of the image
        expected_shape = (730, 600, 3)
        # Check if the image needs to be reshaped
        if image_array.shape == expected_shape:
            reshaped_array = image_array
        else:
            # Resize the image to the expected shape
            resized_image = image.resize((600, 730))
            reshaped_array = np.array(resized_image)
        # Encode the NumPy array to a base64 string
        encoded_string = encode_to_base64(reshaped_array)
        # Encode the text into an image and save it
        encode_text_into_image(encoded_string, _outputImrUri)
        return True
    except FileNotFoundError:
        print(f"Error: Image file not found at path {image_path}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def encode_to_base64(array):
    """
    Encodes a NumPy array to a base64 string.

    Parameters:
    array (np.array): NumPy array to encode.

    Returns:
    str: Base64 encoded string.
    """
    # Convert the NumPy array to an image
    image = Image.fromarray(array.astype('uint8'))
    # Convert the image to bytes
    img_bytes = image.tobytes()
    # Encode the bytes to a base64 string
    encoded_string = base64.b64encode(img_bytes).decode('utf-8')
    return encoded_string

def encode_text_into_image(text, image_path):
    """
    Encodes text into an image using lines.

    Parameters:
    text (str): Text to encode into the image.
    image_path (str): Path to save the encoded image.
    """
    # Define the dimensions of the image
    width = 9000
    height = 9000
    # Create a new black image
    image = Image.new('RGB', (width, height), color='black')
    draw = ImageDraw.Draw(image)
    font_size = 0.5
    font = ImageFont.truetype('arial.ttf', font_size)
    line_spacing = 6
    x, y = line_spacing, line_spacing

    # Encode each character of the text into the image
    for char in text:
        color = (ord(char), ord(char) // 2, ord(char) // 3)
        draw.line([(x, y), (x + font_size, y)], fill=color, width=2)
        x += line_spacing + font_size
        if x + line_spacing > width:
            x = line_spacing
            y += line_spacing + font_size

    # Save the encoded image
    image.save(image_path)

def createImr(_imgUrin, _outputImrUri):
    """
    Entry function to read the actual JPEG file and create an IMR file.

    Parameters:
    _imgUrin (str): Path to the input JPEG file.
    _outputImrUri (str): Path to save the encoded IMR file.

    Returns:
    str: Path to the encoded IMR file if successful, None otherwise.
    """
    # Load the image, encode it, and save it as an IMR file
    if load_image_and_save_as_npy(_imgUrin, _outputImrUri):
        return _outputImrUri
    else:
        return None
