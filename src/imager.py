from PIL import Image


# assumption
# dimensions 1920 x 1080
# square size 4x4
# fps 30
# bits per frame: (1920×1080)/(4×4) = 129,600
chunk_size = 129_600


# split bit stream so we can fit it into a frame. each frame can contain 129600 bits
def split_bit_stream(bits, chunk_size):
    return [bits[i:i+chunk_size] for i in range(0, len(bits), chunk_size)]



def bits_to_image(bit_string):
    # Define color mapping
    color_mapping = {
        "00": (255, 0, 0),    # Red
        "01": (0, 255, 0),    # Green
        "11": (0, 0, 255),    # Blue
        "10": (255, 255, 255)  # White
    }

    # Create a new image with the specified size
    width, height = 1920, 1080
    image = Image.new("RGB", (width, height))

    # Iterate through the bit string and create pixels
    pixel_size = 4
    index = 0
    for y in range(0, height, pixel_size):
        for x in range(0, width, pixel_size):
            # Extract 2 bits from the bit string
            bits = bit_string[index:index+2]
            index += 2

            # Stop if there are not enough bits
            if len(bits) < 2:
                break

            # Map bits to color
            color = color_mapping.get(bits, (0, 0, 0))

            # Fill the 4x4 pixel block with the mapped color
            for dy in range(pixel_size):
                for dx in range(pixel_size):
                    image.putpixel((x + dx, y + dy), color)

    # Save the image
    image.save("output_image.png")




