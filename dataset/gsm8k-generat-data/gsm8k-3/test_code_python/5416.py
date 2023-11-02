def solution():
    """The size of a bathroom is 96 sq ft. If the width of the bathroom is 8 feet and the owner wants to extend it by 2 feet on each side, what is the new area of the bathroom?"""
    # Define the current width and length of the bathroom
    current_width = 8
    current_length = 12 # 96/8 = 12

    # Define the amount of extension on each side
    extension = 2

    # Calculate the new width and length of the bathroom
    new_width = current_width + 2*extension
    new_length = current_length + 2*extension

    # Calculate the new area of the bathroom
    new_area = new_width * new_length

    # Display the new area of the bathroom
    result = new_area
    return result

print(solution())