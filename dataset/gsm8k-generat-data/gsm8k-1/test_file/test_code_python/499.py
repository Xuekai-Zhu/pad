def solution():
    """The rug is 5 feet wider than the chair. The couch is 2 feet longer than twice the width of the rug. If the chair is 3 feet wide. How many feet long is the couch?"""
    chair_width = 3
    rug_width = chair_width + 5
    rug_length = 2 * rug_width
    couch_length = (2 * rug_width) + 2
    result = couch_length
    return result

print(solution())