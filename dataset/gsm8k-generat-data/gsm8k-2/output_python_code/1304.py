def solution():
    """Randy has 1 more baseball glove than 7 times the number of bats he has. If he has 29 baseball gloves, how many bats does he have?"""
    num_gloves = 29
    num_bats = (num_gloves - 1) / 7
    result = num_bats
    return result

print(solution())