def solution():
    # Calculate the number of sweets kept by the mother
    kept_sweets = 27 * (1/3)
    # Calculate the number of sweets divided among the children
    divided_sweets = 27 - kept_sweets
    # Calculate the number of sweets the youngest child got
    youngest_sweets = (1/2) * 8
    # Calculate the total number of sweets the two youngest children got
    total_sweets = youngest_sweets * 2
    # Calculate the number of sweets the second child got
    second_child_sweets = divided_sweets - total_sweets
    result = second_child_sweets
    return result

print(solution())