def solution():
    """A mother buys a box of sweets. She kept 1/3 of the sweets and divided the rest between her 3 children. The eldest got 8 sweets while the youngest got half as many. If there are 27 pieces of sweets in the box, how many sweets did the second child get?"""
    total_sweets = 27
    kept_sweets = total_sweets / 3
    divided_sweets = total_sweets - kept_sweets
    eldest_sweets = 8
    youngest_sweets = eldest_sweets / 2
    second_child_sweets = (divided_sweets - eldest_sweets - youngest_sweets) / 2
    result = second_child_sweets
    return result

print(solution())