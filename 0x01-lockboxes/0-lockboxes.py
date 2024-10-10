#!/usr/bin/python3
'''
    A method that determines if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    '''
    The method
    '''
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for key in range(1, len(boxes) - 1):
        has_key = False
        for idx in range(len(boxes)):
            has_key = key in boxes[idx] and key != idx
            if has_key:
                break
        if has_key is False:
            return has_key
    return True
