#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Method that determines if a given data set represents a valid UTF-8"""
    # Loop over each byte in the data
    i = 0
    while i < len(data):
        # Determine the number of bytes in the current character
        if (data[i] & 0b10000000) == 0b00000000:
            # 1-byte character
            length = 1
        elif (data[i] & 0b11100000) == 0b11000000:
            # 2-byte character
            length = 2
        elif (data[i] & 0b11110000) == 0b11100000:
            # 3-byte character
            length = 3
        elif (data[i] & 0b11111000) == 0b11110000:
            # 4-byte character
            length = 4
        else:
            # Invalid byte sequence
            return False

        # Check that the next length-1 bytes start with 0b10xxxxxx
        for j in range(i+1, i+length):
            if j >= len(data) or (data[j] & 0b11000000) != 0b10000000:
                return False

        # Move to the next character
        i += length

    # If we reached the end of the data, it is a valid UTF-8 sequence
    return True
