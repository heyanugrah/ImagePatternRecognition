# ImagePatternRecognition (IPR Code)

This script offers functions for encoding or creating images into IPR Codes, reading or decoding such images, and producing images that are normal again.

<img src="https://github.com/heyanugrah/ImagePatternRecognition/blob/main/ipr_functionality.jpg" alt="Alt Text" width="600" height="400">

## Functions

### 1. `read_tranformed_image(image_path)`

Reads and decodes text from an encoded image.

- **Parameters:**
  - `image_path` (str): Path to the encoded image file.

- **Returns:**
  - `str`: Decoded and cleaned string from the image.

### 2. `decode_text_from_image(image_path)`

Decodes text from an image encoded using lines.

- **Parameters:**
  - `image_path` (str): Path to the encoded image file.

- **Returns:**
  - `str`: Decoded text from the image.

### 3. `readIpr(_imrActualFile, _outputFileUri)`

Reads and decodes an image from an encoded IMR file.

- **Parameters:**
  - `_imrActualFile` (str): Path to the encoded IMR file.
  - `_outputFileUri` (str): Path to save the decoded image.

### 4. `decode_base64(encoded_string)`

Decodes a base64 encoded string to a NumPy array.

- **Parameters:**
  - `encoded_string` (str): Base64 encoded string.

- **Returns:**
  - `np.array`: Decoded NumPy array.

### 5. `save_decoded_image(array, output_file)`

Saves a decoded NumPy array as an image file.

- **Parameters:**
  - `array` (np.array): Decoded NumPy array.
  - `output_file` (str): Path to save the decoded image.

### 6. `load_image_and_save_as_npy(image_path, _outputImrUri)`

Loads an image, reshapes it, encodes it to base64, and saves it as an IMR file.

- **Parameters:**
  - `image_path` (str): Path to the input image file.
  - `_outputImrUri` (str): Path to save the encoded IMR file.

- **Returns:**
  - `bool`: True if successful, False otherwise.

### 7. `encode_to_base64(array)`

Encodes a NumPy array to a base64 string.

- **Parameters:**
  - `array` (np.array): NumPy array to encode.

- **Returns:**
  - `str`: Base64 encoded string.

### 8. `encode_text_into_image(text, image_path)`

Encodes text into an image using lines.

- **Parameters:**
  - `text` (str): Text to encode into the image.
  - `image_path` (str): Path to save the encoded image.

### 9. `createIpr(_imgUrin, _outputImrUri)`

Entry function to read the actual JPEG file and create an IMR file.

- **Parameters:**
  - `_imgUrin` (str): Path to the input JPEG file.
  - `_outputImrUri` (str): Path to save the encoded IMR file.

- **Returns:**
  - `str`: Path to the encoded IMR file if successful, None otherwise.

## Python Packages Used

This script utilizes the following Python packages:
- `numpy`
- `Pillow` (Python Imaging Library, forked as Pillow)

Ensure these packages are installed in your Python environment to use this script.

## Installation

To install the necessary packages, run the following command:

```bash
pip install numpy Pillow
```

## Usage

Encoding/Writing an Image

```python
createIpr("input_image.jpg", "encoded_image.imr")
```

Decoding/Reading an Image:

```python
readIpr("encoded_image.imr", "decoded_image.jpg")
```

# Encoding and Decoding Images with IPRCode

Learn how to use, a Python module for encoding and decoding images using IPR files.

## Example Usage

### Encoding an Image to IPR File

To encode an image to an IPR file, use the `createIpr` function from the `PatternIprCode` module:

```python
import patternIprCode as ipr

# Create an IPR file with selected image file
encoded_ipr_path = ipr.createIpr(
    r'..\image.jpg',
    r'..\ipr_code.png'
)
```

### Decoding an Image:

Decoding an IPR File Back to Image
To decode an IPR file back to an image, use the readImr function from the patternIprCode module:

```python

import patternIprCode as ipr

# Read an image from an IPR image file
ipr.readIpr(r"..\ipr_code.png", r"../decoded_image.jpg")
```

### Contributing
Contributions are welcome! If you'd like to contribute, fork the repository, make your changes, and submit a pull request. Please ensure your code follows the coding standards and includes appropriate documentation.

### License
This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the LICENSE file for details.


###This README provides a comprehensive overview of the project, including details about the modules and packages used, and instructions for using the functions provided. Feel free to modify it to suit your needs.
