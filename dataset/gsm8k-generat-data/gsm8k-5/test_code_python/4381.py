def solution():
    unfolded_area = 8 * 8  # Each picnic blanket has an unfolded area of 8x8 = 64 square feet
    total_area = 48  # The total folded area of all three blankets is 48 square feet

    # Calculate the folded area of each blanket
    folded_area = total_area / 3

    # Calculate the number of folds required to reduce the area from unfolded area to folded area
    num_folds = round(math.log(folded_area / unfolded_area, 2))
    result = num_folds
    return result

print(solution())