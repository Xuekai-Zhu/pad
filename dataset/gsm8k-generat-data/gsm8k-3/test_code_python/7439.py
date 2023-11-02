def solution():
    """Of 96 oranges, half were ripe. If 1/4 of the ripe oranges were eaten and 1/8 of the unripe oranges were eaten, how many were left eaten in total?"""
    # Calculate the number of ripe oranges
    ripe_oranges = 96 / 2

    # Calculate the number of unripe oranges
    unripe_oranges = 96 / 2

    # Calculate the number of ripe oranges that were eaten
    ripe_eaten = ripe_oranges / 4

    # Calculate the number of unripe oranges that were eaten
    unripe_eaten = unripe_oranges / 8

    # Calculate the total number of oranges that were eaten
    total_eaten = ripe_eaten + unripe_eaten

    # Calculate the number of oranges left uneaten
    uneaten = 96 - total_eaten

    # Display the number of oranges left uneaten
    result = uneaten
    return result

print(solution())