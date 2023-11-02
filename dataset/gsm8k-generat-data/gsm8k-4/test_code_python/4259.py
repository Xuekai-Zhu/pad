def solution():
    """A mother buys a box of sweets. She kept 1/3 of the sweets and divided the rest between her 3 children. The eldest got 8 sweets while the youngest got half as many. If there are 27 pieces of sweets in the box, how many sweets did the second child gets?"""
    # Define the total number of sweets in the box
    total_sweets = 27

    # Calculate the number of sweets kept by the mother
    mother_sweets = total_sweets / 3

    # Calculate the number of sweets left to be divided between the children
    remaining_sweets = total_sweets - mother_sweets

    # Calculate the number of sweets the youngest child got
    youngest_sweets = remaining_sweets / 6

    # Calculate the number of sweets the eldest child got
    eldest_sweets = 8

    # Calculate the number of sweets the second child got
    second_sweets = remaining_sweets - youngest_sweets - eldest_sweets

    # return the result
    result = second_sweets
    return result

print(solution())