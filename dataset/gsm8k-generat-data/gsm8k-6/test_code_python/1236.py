def solution():
    # Calculate the number of black cats
    black_cats = round(0.25 * 16)  # 25% of the cats are black

    # Calculate the number of grey cats
    grey_cats = 16 - 2 - black_cats  # subtract the number of white and black cats from total

    result = grey_cats
    return result

print(solution())