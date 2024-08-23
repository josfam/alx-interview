#!/usr/bin/python3

"""Contains function that determines whether the provided data represents
valid UTF-8 encoding"""


def validUTF8(data):
    """Determines whether the provided data represents UTF-8 encoding"""
    MAX_BITS = 8
    MAX_CONT_BYTES = 6
    padded = [str(bin(num)).lstrip('0b')[-MAX_BITS:].zfill(8) for num in data]

    cont_bytes_after = 0
    cont_bytes_got = 0
    i = 0

    while i < len(padded):
        num = padded[i]

        if num.startswith('0'):  # normal ASCII letter
            pass
        elif num.startswith('11'):  # multibyte
            cont_bytes_after = num.find('0') - 1
            if cont_bytes_after > MAX_CONT_BYTES:
                return False
            # check expected continuation bytes
            cont_bytes = padded[i + 1: i + cont_bytes_after + 1]
            if not cont_bytes: # no more bytes exist
                return False
            i += 1 # move to the first continuation byte
            for cont_byte in cont_bytes:
                if not cont_byte.startswith('10'):  # illegal continuation
                    return False
                cont_bytes_got += 1
                i += 1
            if not cont_bytes_got == cont_bytes_after:
                return False
            cont_bytes_got = 0
        else:  # starts with 10 (misplaced continuation byte)
            return False
        i += 1

    return True
