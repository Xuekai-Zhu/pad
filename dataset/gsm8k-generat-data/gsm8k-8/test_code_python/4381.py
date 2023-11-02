def solution():
    # Calculate the area of one unfolded blanket
    blanket_area = 8 * 8

    # Calculate the total area of all three blankets
    total_area = 48

    # Calculate the number of times the blankets were folded
    num_folds = int(math.log(total_area/blanket_area, 2))

    result = num_folds
    return result

print(solution())