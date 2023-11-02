def solution():
    """There are 14 red crayons, 5 more blue crayons than red crayons, and 6 less yellow crayons than double the blue crayons. How many yellow crayons are there?"""
    # Define the number of red crayons
    red_crayons = 14

    # Calculate the number of blue crayons
    blue_crayons = red_crayons + 5

    # Calculate twice the number of blue crayons
    double_blue_crayons = blue_crayons * 2

    # Calculate the number of yellow crayons
    yellow_crayons = double_blue_crayons - 6

    # return the result
    result = yellow_crayons
    return result

print(solution())