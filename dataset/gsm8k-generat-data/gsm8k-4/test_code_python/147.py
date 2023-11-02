def solution():
    """Mary has 5 green crayons and 8 blue crayons of different shades. If she gives out 3 green crayons and 1 blue crayon to Becky, how many crayons does she have left?"""
    # Define the initial number of green and blue crayons
    green_crayons = 5
    blue_crayons = 8

    # Define the number of green and blue crayons given to Becky
    green_given = 3
    blue_given = 1

    # Calculate the remaining number of green and blue crayons
    green_remaining = green_crayons - green_given
    blue_remaining = blue_crayons - blue_given

    # return the result
    result = green_remaining + blue_remaining
    return result

print(solution())