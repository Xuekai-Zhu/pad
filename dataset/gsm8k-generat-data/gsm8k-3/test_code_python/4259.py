def solution():
    """A mother buys a box of sweets. She kept 1/3 of the sweets and divided the rest between her 3 children. The eldest got 8 sweets while the youngest got half as many. If there are 27 pieces of sweets in the box, how many sweets did the second child get?"""
    # Calculate the number of sweets the mother kept
    mother_kept = 27 / 3

    # Calculate the number of sweets divided among the children
    children_sweets = 27 - mother_kept

    # Calculate the number of sweets the youngest child got
    youngest_sweets = children_sweets / 3 / 2

    # Calculate the number of sweets the second child got
    second_sweets = children_sweets / 3 - youngest_sweets

    # Display the number of sweets the second child got
    result = second_sweets
    return result

print(solution())