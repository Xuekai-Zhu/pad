def solution():
    """Mark can jump 6 inches off the ground. Lisa can jump double the height as Mark, and Jacob can jump double the height of Lisa. If James jumps 2/3 as high Jacob, how high can James jump?"""
    # Define Mark's jumping height
    mark_height = 6

    # Define Lisa's jumping height
    lisa_height = mark_height * 2

    # Define Jacob's jumping height
    jacob_height = lisa_height * 2

    # Define James's jumping height
    james_height = jacob_height * (2/3)

    result = james_height
    return result

print(solution())