def solution():
    # Calculate the number of sweets the mother kept
    total_sweets = 27
    mother_sweets = total_sweets / 3

    # Calculate the number of sweets divided between the three children
    child_sweets = total_sweets - mother_sweets
    # Calculate the number of sweets the eldest child got
    eldest_sweets = 8
    # Calculate the number of sweets the youngest child got
    youngest_sweets = 0.5 * eldest_sweets

    # Calculate the number of sweets the second child got
    second_child_sweets = child_sweets - (eldest_sweets + youngest_sweets)
    result = second_child_sweets
    return result

print(solution())