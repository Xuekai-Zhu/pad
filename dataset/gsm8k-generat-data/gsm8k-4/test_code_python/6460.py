def solution():
    """Brian has the same percentage of white stones and black stones in his collection of 100 stones as he does of grey stones and green stones in a separate collection. He has 40 grey stones and 60 green stones. How many white stones does Brian have if he has more white stones than black ones?"""
    # Define the number of grey and green stones
    grey_stones = 40
    green_stones = 60

    # Calculate the total number of stones in the separate collection
    total_stones = grey_stones + green_stones

    # Calculate the percentage of grey stones and green stones in the separate collection
    grey_percentage = grey_stones / total_stones
    green_percentage = green_stones / total_stones

    # Calculate the number of white stones and black stones in the main collection
    total_main_stones = 100
    white_stones = black_stones = total_main_stones / 2

    # Calculate the percentage of white stones and black stones in the main collection
    white_percentage = white_stones / total_main_stones
    black_percentage = black_stones / total_main_stones

    # Determine the color of stone that is represented by the same percentage in both collections
    if grey_percentage == white_percentage:
        brian_color = "white"
    else:
        brian_color = "black"

    # Determine the number of white stones that Brian has
    if brian_color == "white":
        white_stones = max(white_stones, black_stones)
    else:
        white_stones = total_main_stones - max(white_stones, black_stones)

    # return the result
    result = white_stones
    return result

print(solution())