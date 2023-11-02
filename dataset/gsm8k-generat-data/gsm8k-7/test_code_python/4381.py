def solution():
    unfolded_area = 8 * 8  # area of one unfolded blanket
    total_area = 48  # total area of all folded blankets
    folded_area = total_area / 3
    num_folds = (unfolded_area - folded_area) / unfolded_area  # formula for calculating number of folds
    result = num_folds
    return result

print(solution())