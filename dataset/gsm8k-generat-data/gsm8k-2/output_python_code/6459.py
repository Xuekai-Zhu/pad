def solution():
    """Brian has the same percentage of white stones and black stones in his collection of 100 stones as he does of grey stones and green stones in a separate collection. He has 40 grey stones and 60 green stones. How many white stones does Brian have if he has more white stones than black ones?"""
    grey_stones = 40
    green_stones = 60
    total_grey_green = grey_stones + green_stones
    white_black_ratio = (100 - total_grey_green) / total_grey_green
    
    # Let's assume Brian has x white stones
    x = 0
    while True:
        x += 1
        black_stones = x * white_black_ratio
        if x > black_stones and x > grey_stones:
            break

    result = x
    return result

print(solution())