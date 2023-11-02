def solution():
    total_sweets = 27
    mother_kept = total_sweets / 3
    remaining_sweets = total_sweets - mother_kept

    # Determine the total number of sweets divided between the 3 children
    child_sweets = remaining_sweets / 3

    # Determine the number of sweets given to the youngest child
    youngest_child_sweets = child_sweets / 2

    # Determine the number of sweets given to the eldest child
    eldest_child_sweets = 8

    # Determine the number of sweets given to the second child
    second_child_sweets = remaining_sweets - (youngest_child_sweets + eldest_child_sweets)

    result = second_child_sweets

    return result

print(solution())