#!/usr/bin/python3


"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Method to determine if a given data set represents a valid UTF-8 encoding.
    Args:
        data: List of integers where each integer represents a byte (0-255).
    Returns:
        True if the data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get the binary representation. Remove the '0b' prefix.
        bin_rep = bin(num)[2:].rjust(8, '0')

        if n_bytes == 0:
            # Count the number of leading 1's
            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1

            # 1-byte character
            if n_bytes == 0:
                continue

            # UTF-8 characters can be 1 to 4 bytes long
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if it is a valid continuation byte
            if not (int(bin_rep[0]) == 1 and int(bin_rep[1]) == 0):
                return False

        # Decrement the number of bytes left to check
        n_bytes -= 1

    # If there are no more bytes expected
    return n_bytes == 0
