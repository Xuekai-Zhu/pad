def solution():
    """A rectangle has a length of 40 meters and a width of 20 meters. A similar smaller rectangle has half the length and width of the big rectangle. What's the area of the smaller rectangle?"""
    # Define the length and width of the big rectangle
    big_length = 40
    big_width = 20

    # Calculate the length and width of the smaller rectangle
    small_length = big_length / 2
    small_width = big_width / 2

    # Calculate the area of the smaller rectangle
    small_area = small_length * small_width

    # return the result
    result = small_area
    return result

print(solution())