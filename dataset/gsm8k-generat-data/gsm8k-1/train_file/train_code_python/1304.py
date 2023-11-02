def solution():
    """Randy has 1 more baseball glove than 7 times the number of bats he has. If he has 29 baseball gloves, how many bats does he have?"""
    glove_count = 29
    bat_count = (glove_count - 1) / 7
    result = bat_count
    return result

print(solution())