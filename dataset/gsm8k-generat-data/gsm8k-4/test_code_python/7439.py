def solution():
    """Of 96 oranges, half were ripe. If 1/4 of the ripe oranges were eaten and 1/8 of the unripe oranges were eaten, how many were left uneaten in total?"""
    # Define the total number of oranges and the number of ripe oranges
    total_oranges = 96
    ripe_oranges = total_oranges / 2

    # Calculate the number of ripe oranges that were eaten
    eaten_ripe_oranges = ripe_oranges / 4

    # Calculate the number of unripe oranges that were eaten
    unripe_oranges = total_oranges - ripe_oranges
    eaten_unripe_oranges = unripe_oranges / 8

    # Calculate the total number of oranges that were eaten
    total_eaten = eaten_ripe_oranges + eaten_unripe_oranges

    # Calculate the total number of oranges that were left uneaten
    total_uneaten = total_oranges - total_eaten

    # return the result
    result = total_uneaten
    return result

print(solution())