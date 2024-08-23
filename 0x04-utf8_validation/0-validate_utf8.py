#!/usr/bin/python3

"""Contains function that determines whether the provided data represents
valid UTF-8 encoding"""


def validUTF8(data):
    """Determines whether the provided data represents UTF-8 encoding"""
    MAX_BITS = 8
    MAX_CONT_BYTES = 3
    padded = [
        str(bin(num)).lstrip('0b')[-MAX_BITS:].zfill(MAX_BITS)
        for num in data
    ]

    cont_bytes_expected = 0
    i = 0

    while i < len(padded):
        num = padded[i]

        if num.startswith('0'):  # normal ASCII letter
            pass
        elif num.startswith('11'):  # multibyte
            cont_bytes_expected = num.find('0') - 1
            if cont_bytes_expected > MAX_CONT_BYTES:
                return False
            # check expected continuation bytes
            cont_bytes = padded[i + 1: i + cont_bytes_expected + 1]
            valid_conts = [
                1 if byte.startswith('10') else 0
                for byte in cont_bytes
            ]

            if not cont_bytes \
                or not all(valid_conts) \
                    or not len(valid_conts) == cont_bytes_expected:
                return False

            i += len(valid_conts)  # skip to the last continuation byte
        else:  # starts with 10 (misplaced continuation byte)
            return False
        i += 1

    return True
