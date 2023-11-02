def solution():
    num_gloves = 29

    # Let x be the number of bats Randy has
    # According to the problem, num_gloves = 1 + 7x
    x = (num_gloves - 1) / 7

    result = x
    return result

print(solution())