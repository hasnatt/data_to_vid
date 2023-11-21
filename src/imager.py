from PIL import Image
import cv2
import os


# assumption
# dimensions 1920 x 1080
# square size 4x4
# fps 30
# bits per frame: (1920×1080)/(4×4) = 129,600



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
    return image


def images_to_video(images_folder, output_video_path, fps=30, file_extension=".png"):
    # Get the list of image files in the directory
    image_files = [img for img in os.listdir(images_folder) if img.endswith(file_extension)]

    # Sort the image files to ensure the correct order
    image_files.sort()

    # Get the first image to extract its dimensions
    first_image = cv2.imread(os.path.join(images_folder, image_files[0]))
    height, width, _ = first_image.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can also use 'XVID' or 'MJPG' codecs
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Iterate through the images and write them to the video file
    for image_file in image_files:
        image_path = os.path.join(images_folder, image_file)
        frame = cv2.imread(image_path)
        video_writer.write(frame)

    # Release the VideoWriter object
    video_writer.release()

    # print(f"Video created successfully at {output_video_path}")




