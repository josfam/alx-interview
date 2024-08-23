#!/usr/bin/python3

"""Contains function that determines whether the provided data represents
valid UTF-8 encoding"""


def validUTF8(data):
    """Determines whether the provided data represents UTF-8 encoding"""
    MAX_BITS = 8
    padded = [str(bin(num)).lstrip('0b').zfill(8) for num in data]

    is_multibyte = False
    cont_bytes_expected = 0
    cont_bytes_got = 0
    i = 0

    while i < len(padded):
        num = padded[i]

        if len(num) > MAX_BITS:  # more than 8 bits is too many
            return False
        if num.startswith('0'):  # normal ASCII letter
            pass
        elif num.startswith('11'):  # multibyte
            cont_bytes_expected = num.find('0')
            if cont_bytes_expected > 6: # max possible
                return False
            # look at the next cont_bytes_expected numbers
            cont_bytes = padded[i + 1: i + cont_bytes_expected + 1]
            i += 1
            for cont_byte in cont_bytes:
                if not cont_byte.startswith('10'):  # illegal continuation
                    return False
                cont_bytes_got += 1
                i += 1
        else:  # starts with 10 (misplaced continuation byte)
            return False
        i += 1

    return True
