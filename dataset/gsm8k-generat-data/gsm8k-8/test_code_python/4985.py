def solution():
    # Define the dimensions of the bigger rectangle
    big_length = 40
    big_width = 20

    # Calculate the dimensions of the smaller rectangle
    small_length = big_length / 2
    small_width = big_width / 2

    # Calculate the area of the smaller rectangle
    small_area = small_length * small_width
    result = small_area
    return result

print(solution())