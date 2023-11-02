def solution():
    """A rectangle has a length of 40 meters and a width of 20 meters. A similar smaller rectangle has half the length and width of the big rectangle. What's the area of the smaller rectangle?"""
    # Define the dimensions of the big rectangle
    big_length = 40
    big_width = 20

    # Calculate the dimensions of the small rectangle
    small_length = big_length / 2
    small_width = big_width / 2

    # Calculate the area of the small rectangle
    small_area = small_length * small_width

    # Display the area of the small rectangle
    result = small_area
    return result

print(solution())