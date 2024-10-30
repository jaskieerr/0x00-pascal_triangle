#!/usr/bin/python3
'''utf8 validation'''

def validUTF8(data):
    '''utf8 validation'''
    remaining = 0
    length = len(data)
    for idx in range(length):
        if remaining > 0:
            remaining -= 1
            continue
        if type(data[idx]) is not int or data[idx] < 0 or data[idx] > 0x10FFFF:
            return False
        elif data[idx] <= 0x7F:
            remaining = 0
        elif data[idx] & 0b11111000 == 0b11110000:
            bytes_needed = 4
            if length - idx >= bytes_needed:
                next_bytes = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[idx + 1: idx + bytes_needed],
                ))
                if not all(next_bytes):
                    return False
                remaining = bytes_needed - 1
            else:
                return False
        elif data[idx] & 0b11110000 == 0b11100000:
            bytes_needed = 3
            if length - idx >= bytes_needed:
                next_bytes = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[idx + 1: idx + bytes_needed],
                ))
                if not all(next_bytes):
                    return False
                remaining = bytes_needed - 1
            else:
                return False
        elif data[idx] & 0b11100000 == 0b11000000:
            bytes_needed = 2
            if length - idx >= bytes_needed:
                next_bytes = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[idx + 1: idx + bytes_needed],
                ))
                if not all(next_bytes):
                    return False
                remaining = bytes_needed - 1
            else:
                return False
        else:
            return False
    return True
