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
        raise ValueError("Message is too long to hide in the image.")

    # Add end of message marker
    binary_message += '11111111'

    # Convert image to list of pixels
    pixels = list(image.getdata())

    # Modify pixels to hide the message
    new_pixels = []
    binary_index = 0
    for pixel in pixels:
        r, g, b = pixel
        if binary_index < len(binary_message):
            r = (r & ~1) | int(binary_message[binary_index])
            binary_index += 1
        if binary_index < len(binary_message):
            g = (g & ~1) | int(binary_message[binary_index])
            binary_index += 1
        if binary_index < len(binary_message):
            b = (b & ~1) | int(binary_message[binary_index])
            binary_index += 1
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
    end_marker_found = False
    for pixel in pixels:
        if end_marker_found:
            break
        r, g, b = pixel
        bits_from_pixel = [r & 1, g & 1, b & 1]
        for bit in bits_from_pixel:
            if len(binary_message) % 8 == 0 and binary_message.endswith('11111111'):
                end_marker_found = True
                break
            else:
                binary_message += str(bit)

    # Convert binary message to string without the end marker
    message = binary_to_message(binary_message[:-8])
    return message