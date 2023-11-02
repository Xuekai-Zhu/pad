def solution():
    """Mark can jump 6 inches off the ground. Lisa can jump double the height as Mark, and Jacob can jump double the height of Lisa. If James jumps 2/3 as high Jacob, how high can James jump?"""
    mark_jump = 6
    lisa_jump = mark_jump * 2
    jacob_jump = lisa_jump * 2
    james_jump = jacob_jump * (2/3)
    result = james_jump
    return result

print(solution())