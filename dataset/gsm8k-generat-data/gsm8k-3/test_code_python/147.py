def solution():
    """Mary has 5 green crayons and 8 blue crayons of different shades. If she gives out 3 green crayons and 1 blue crayon to Becky, how many crayons does she have left?"""
    # Define the initial number of green and blue crayons
    green_crayons = 5
    blue_crayons = 8

    # Define the number of green and blue crayons Mary gives to Becky
    green_given = 3
    blue_given = 1

    # Subtract the number of crayons given to Becky from the initial number
    green_crayons -= green_given
    blue_crayons -= blue_given

    # Return the remaining number of green and blue crayons
    result = (green_crayons, blue_crayons)
    return result

print(solution())