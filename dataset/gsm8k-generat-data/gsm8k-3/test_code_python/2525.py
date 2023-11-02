def solution():
    """There are 14 red crayons, 5 more blue crayons than red crayons, and 6 less yellow crayons than double the blue crayons.  How many yellow crayons are there?"""
    # Define the number of red crayons
    red_crayons = 14

    # Calculate the number of blue crayons
    blue_crayons = red_crayons + 5

    # Calculate the number of yellow crayons
    yellow_crayons = 2 * blue_crayons - 6

    # Display the number of yellow crayons
    result = yellow_crayons
    return result

print(solution())