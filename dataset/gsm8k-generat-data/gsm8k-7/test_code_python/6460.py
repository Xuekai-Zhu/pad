def solution():
    num_grey_stones = 40
    num_green_stones = 60
    total_stones = 100

    # Calculate the percentage of grey and green stones
    grey_percentage = num_grey_stones / total_stones
    green_percentage = num_green_stones / total_stones

    # Find the percentage of white stones (assumed to be equal to black stones)
    white_percentage = (grey_percentage + green_percentage) / 2

    # Calculate the number of white stones
    num_white_stones = white_percentage * total_stones

    # Check if there are more white stones than black stones
    num_black_stones = num_white_stones
    if num_white_stones <= total_stones / 2:
        num_black_stones += 1

    result = num_white_stones
    return result

print(solution())