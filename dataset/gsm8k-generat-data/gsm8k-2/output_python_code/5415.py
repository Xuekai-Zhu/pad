def solution():
    """The size of a bathroom is 96 sq ft. If the width of the bathroom is 8 feet and the owner wants to extend it by 2 feet on each side, what is the new area of the bathroom?"""
    old_area = 96
    old_width = 8
    new_width = old_width + 4  # add 2 feet on each side
    new_length = old_area / old_width  # calculate old length
    new_area = new_length * new_width
    result = new_area
    return result

print(solution())