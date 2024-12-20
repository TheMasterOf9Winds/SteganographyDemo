from PIL import Image

def message_to_binary(message):
    """Converts a string message to a binary string."""
    binary = ''.join(format(ord(char), '08b') for char in message)
    binary = binary.replace(' ', '')
    return binary

def binary_to_message(binary):
    """Converts a binary string to a string message."""
    separated_binary = [binary[i:i+8] for i in range(0, len(binary), 8)]
    message = ''.join(chr(int(byte, 2)) for byte in separated_binary)
    return message

def hide_message_in_image(image_file, message):
    """Hides a message within an image using steganography."""

    # Convert message to binary string
    binary_message = message_to_binary(message)

    # Open image file
    image = Image.open(image_file)

    # Convert image to RGB format
    image = image.convert('RGB')

    # Get image dimensions
    width, height = image.size

    # Maximum number of characters to hide
    max_chars = width * height * 3 // 8

    # Check if message is too long
    if len(binary_message) > max_chars:
        raise ValueError("Message too long to hide in image.")
    
    # Add end of message marker
    binary_message += '11111111'

    # Hide message in image pixels
    pixels = list(image.getdata())
    new_pixels = []
    bit_count = 0

    for pixel in pixels:
        r, g, b = pixel
        if bit_count < len(binary_message):
            r = (r & ~1) | int(binary_message[bit_count])
            bit_count += 1
        if bit_count < len(binary_message):
            g = (g & ~1) | int(binary_message[bit_count])
            bit_count += 1
        if bit_count < len(binary_message):
            b = (b & ~1) | int(binary_message[bit_count])
            bit_count += 1
        new_pixels.append((r, g, b))

    # Create a new image with the modified pixels
    new_image = Image.new('RGB', (width, height))
    new_image.putdata(new_pixels)
    new_image.save('hidden_message_image.png')

def reveal_message_in_image(image_file):
    """Reveals a hidden message within an image using steganography."""

    # Open image file
    image = Image.open(image_file)
    # Convert image to RGB format
    image = image.convert('RGB')

    # Get image dimensions
    width, height = image.size

    # Extract message from image pixels
    pixels = list(image.getdata())
    binary_message = ''
    char_count = 0
    current_byte = 0
    for pixel in pixels:
        r, g, b = pixel
        if char_count < 8:
            current_bit = b % 2
            current_byte = current_byte * 2 + current_bit
            char_count += 1
            if char_count == 8:
                if current_byte == 255:
                    break
                binary_message += chr(current_byte)
                current_byte = 0
                char_count = 0
    
    # Convert binary message to string message
    message = binary_to_message(binary_message)
    return message