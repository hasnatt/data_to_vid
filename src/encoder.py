file = 'pic.JPG'

def file_to_bits(file_path):
    try:
        with open(file_path, 'rb') as file:
            # Read the entire file content
            file_content = file.read()

            # Convert each byte to its binary representation
            bits = ''.join(format(byte, '08b') for byte in file_content)

            return bits
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
bits = file_to_bits(file)

if bits:
    # print(f"Binary representation of {file_path}:\n{bits}")
    with open("picjpg.txt", 'w') as file:
    # Write the content to the file
        file.write(bits)

