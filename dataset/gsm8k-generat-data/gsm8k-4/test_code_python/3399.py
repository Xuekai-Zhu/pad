def solution():
    """On an American flag, the first stripe is red and half of the remaining stripes are also red. Each flag has 13 stripes. John buys 10 flags. How many red stripes are there?"""
    # Define the total number of stripes on each flag
    total_stripes = 13

    # Define the number of red stripes on the first flag
    red_stripes = 1

    # Calculate the number of red stripes on the remaining flags
    for i in range(9):
        red_stripes += (total_stripes - red_stripes) / 2

    # Calculate the total number of red stripes on all the flags
    total_red_stripes = red_stripes * 10

    # return the result
    result = total_red_stripes
    return result

print(solution())