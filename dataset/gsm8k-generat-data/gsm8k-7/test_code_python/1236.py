def solution():
    total_cats = 16
    white_cats = 2
    black_cats = int(total_cats * 0.25)

    # Calculate the number of grey cats
    grey_cats = total_cats - white_cats - black_cats
    result = grey_cats
    return result

print(solution())