def solution():
    """The size of a bathroom is 96 sq ft. If the width of the bathroom is 8 feet and the owner wants to extend it by 2 feet on each side, what is the new area of the bathroom?"""
    current_area = 96
    current_width = 8
    new_width = current_width + 4  # 2 feet added to each side
    new_length = current_area / current_width
    new_area = new_width * new_length
    result = new_area
    return result

print(solution())