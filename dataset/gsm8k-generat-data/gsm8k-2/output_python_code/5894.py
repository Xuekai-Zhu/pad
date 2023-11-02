def solution():
    """Mark can jump 6 inches off the ground. Lisa can jump double the height as Mark, and Jacob can jump double the height of Lisa. If James jumps 2/3 as high Jacob, how high can James jump?"""
    mark_height = 6
    lisa_height = 2 * mark_height
    jacob_height = 2 * lisa_height
    james_height = (2 / 3) * jacob_height
    result = james_height
    return result

print(solution())