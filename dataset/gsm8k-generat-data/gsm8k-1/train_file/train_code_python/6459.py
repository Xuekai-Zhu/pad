def solution():
    """Brian has the same percentage of white stones and black stones in his collection of 100 stones as he does of grey stones and green stones in a separate collection. He has 40 grey stones and 60 green stones. How many white stones does Brian have if he has more white stones than black ones?"""
    total_grey_green = 100
    grey_stones = 40
    green_stones = 60
    total_white_black = total_grey_green
    white_stones = total_white_black * (grey_stones + green_stones) / (100 - (grey_stones + green_stones))
    black_stones = total_white_black - white_stones
    if white_stones > black_stones:
        result = white_stones
    else:
        result = black_stones
    return result

print(solution())