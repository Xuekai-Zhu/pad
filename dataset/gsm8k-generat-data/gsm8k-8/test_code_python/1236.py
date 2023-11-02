def solution():
    # Calculate the number of black cats
    black_cats = 0.25 * 16

    # Calculate the number of grey cats
    grey_cats = 16 - 2 - black_cats

    result = grey_cats
    return result

print(solution())