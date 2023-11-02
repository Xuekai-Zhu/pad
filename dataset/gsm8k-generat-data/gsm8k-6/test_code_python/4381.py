def solution():
    # Calculate the total area of the three picnic blankets
    total_area = 8 * 8 * 3

    # Calculate the area of the folded blankets
    folded_area = 48

    # Calculate the number of times the blankets were folded
    folds = total_area // folded_area
    result = folds
    return result

print(solution())