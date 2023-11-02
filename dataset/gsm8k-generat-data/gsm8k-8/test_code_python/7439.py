def solution():
    # Calculate the number of ripe oranges
    ripe_oranges = 96 / 2

    # Calculate the number of unripe oranges
    unripe_oranges = 96 / 2

    # Calculate the number of ripe oranges that were eaten
    eaten_ripe_oranges = ripe_oranges / 4

    # Calculate the number of unripe oranges that were eaten
    eaten_unripe_oranges = unripe_oranges / 8

    # Calculate the total number of oranges that were eaten
    total_eaten_oranges = eaten_ripe_oranges + eaten_unripe_oranges

    # Calculate the number of oranges that were left uneaten
    uneaten_oranges = 96 - total_eaten_oranges

    result = uneaten_oranges
    return result

print(solution())