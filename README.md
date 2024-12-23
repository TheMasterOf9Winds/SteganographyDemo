# SteganographyDemo

## Overview
This project demonstrates the use of steganography to hide messages within images. Steganography is the practice of concealing a message within another medium, such as an image, in such a way that only the intended recipient can detect the presence of the hidden message. This works by storing data in the least significant bit of each R, G, and B value of a pixel; this would mean 3 bits of storage per pixel. Because this only slightly changes the last bit of each RGB value, the difference is negligible.

## Features
- Convert a text message to a binary string.
- Hide a binary message within the least significant bits of an image's pixels.
- Extract a hidden message from an image.

## Requirements
- Python 3.x
- Pillow library (Python Imaging Library fork)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/TheMasterOf9Winds/SteganographyDemo.git
    cd SteganographyDemo
    ```

2. Install the required dependencies:
    ```sh
    pip install pillow
    ```

## Usage

### Hiding a Message
To hide a message within an image, use the `hide_message_in_image` function. This function takes an image file and a message string as input and saves a new image file 'hidden_message_image.png' with the hidden message in the same directory.

NOTE: This will create or overwrite a file named 'hidden_message_image.png' in the same directory when hiding a message.

Example:
```python
from steganography import hide_message_in_image, reveal_message_in_image

# Hide a message
hide_message_in_image('input_image.png', 'Secret Message')

# Extract the hidden message
message = reveal_message_in_image('hidden_message_image.png')
print('Extracted Message:', message)
```

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### Acknowledgements
Pillow - The friendly PIL fork.