def solution():
    """Brian has the same percentage of white stones and black stones in his collection of 100 stones as he does of grey stones and green stones in a separate collection. He has 40 grey stones and 60 green stones. How many white stones does Brian have if he has more white stones than black ones?"""
    # Define the number of grey and green stones
    grey_stones = 40
    green_stones = 60

    # Calculate the percentage of grey and green stones
    total_stones = grey_stones + green_stones
    grey_percentage = (grey_stones / total_stones) * 100
    green_percentage = (green_stones / total_stones) * 100

    # Calculate the number of white stones
    white_percentage = grey_percentage  # Since the percentages are the same for white and black
    white_stones = (white_percentage / 100) * 100

    # Calculate the number of black stones
    black_percentage = 100 - white_percentage
    black_stones = (black_percentage / 100) * 100

    # Check if Brian has more white than black stones
    if white_stones > black_stones:
        result = white_stones
    else:
        result = "Brian has more black stones than white stones."

    return result

print(solution())