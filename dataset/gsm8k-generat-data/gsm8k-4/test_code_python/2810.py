def solution():
    """If there are four times as many red crayons as blue crayons in a box, and there are 3 blue crayons. How many crayons total are in the box?"""
    # Define the number of blue crayons
    blue_crayons = 3

    # Calculate the number of red crayons
    red_crayons = 4 * blue_crayons

    # Calculate the total number of crayons
    total_crayons = blue_crayons + red_crayons

    # return the result
    result = total_crayons
    return result

print(solution())