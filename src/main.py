from bits_handler import decode, encode
from imager import split_bit_stream, bits_to_image

chunk_size = 129600

if __name__ == "__main__":
    file = 'pic.JPG'

    # convert file to bit stream
    file_to_bits = encode(file)
    frames_of_bits = split_bit_stream(file_to_bits, chunk_size)


    bits_to_image(frames_of_bits[5])
    
    

    # decode(frames[0], "test.jpg")