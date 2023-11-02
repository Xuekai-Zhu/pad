def solution():
    """
    A mother buys a box of sweets. She kept 1/3 of the sweets and divided the rest between her 3 children. 
    The eldest got 8 sweets while the youngest got half as many. If there are 27 pieces of sweets in the box, how many sweets did the second child gets?
    """
    total_sweets = 27
    mother_kept = total_sweets // 3
    remaining_sweets = total_sweets - mother_kept
    eldest_sweets = 8
    youngest_sweets = eldest_sweets // 2
    second_child_sweets = (remaining_sweets - eldest_sweets - youngest_sweets) // 2
    result = second_child_sweets
    return result

print(solution())