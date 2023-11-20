def encode(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
            bits = ''.join(format(byte, '08b') for byte in file_content)
            return bits
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def decode(bits, output_file_path):
    try:
        # Ensure the number of bits is a multiple of 8
        padding = len(bits) % 8
        if padding != 0:
            bits = '0' * (8 - padding) + bits

        # Convert bits back to bytes
        bytes_list = [int(bits[i:i+8], 2) for i in range(0, len(bits), 8)]

        with open(output_file_path, 'wb') as output_file:
            for byte in bytes_list:
                output_file.write(bytes([byte]))

        print(f"File successfully decoded and saved as {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")











