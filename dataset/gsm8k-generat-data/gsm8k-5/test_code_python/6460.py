def solution():
    # Calculate the percentage of grey and green stones in the separate collection
    grey_percentage = 40 / 100  # 40 grey stones out of 100
    green_percentage = 60 / 100  # 60 green stones out of 100

    # Determine the percentage of white and black stones in Brian's collection
    white_percentage = max(grey_percentage, green_percentage)
    black_percentage = 1 - white_percentage

    # Calculate the total number of white and black stones in Brian's collection
    total_stones = 100
    white_stones = round(white_percentage * total_stones)
    black_stones = round(black_percentage * total_stones)

    # Ensure that Brian has more white stones than black ones
    if white_stones <= black_stones:
        white_stones = black_stones + 1

    result = white_stones
    return result

print(solution())