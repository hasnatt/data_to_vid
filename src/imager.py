from PIL import Image



def create_image_from_bits(bits, width, height, square_size):
    # Calculate the number of squares in each dimension
    num_squares_x = width // square_size
    num_squares_y = height // square_size

    # Create a new image with white background
    img = Image.new('RGB', (width, height), 'white')
    pixels = img.load()

    # Iterate through bits and draw squares accordingly
    for i in range(len(bits)):
        # Calculate the position of the current square
        row = i // num_squares_x
        col = i % num_squares_x

        # Calculate the coordinates of the square
        x = col * square_size
        y = row * square_size

        # Draw a black square if the bit is 1, otherwise draw a white square
        color = (0, 0, 0) if bits[i] == '1' else (255, 255, 255)

        # Draw the square
        for j in range(square_size):
            for k in range(square_size):
                pixels[x + j, y + k] = color

    return img

# Example usage
bits_string = "11001100110011001100101001010101010101010100101010101010101010101010101001010101010101011100"  # Replace this with your actual bit string
image_width = 1920
image_height = 1080
square_size = 8

image = create_image_from_bits(bits_string, image_width, image_height, square_size)
image.show()
