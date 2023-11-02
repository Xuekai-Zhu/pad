def solution():
    """Emmy has a collection of 14 iPods. She loses 6 out of the 14 she had but she still has twice as many as Rosa. How many iPods does Emmy and Rosa have together?"""
    initial_iPods = 14
    lost_iPods = 6
    remaining_iPods = initial_iPods - lost_iPods
    rosa_iPods = remaining_iPods / 2
    total_iPods = remaining_iPods + rosa_iPods
    result = total_iPods
    return result

print(solution())