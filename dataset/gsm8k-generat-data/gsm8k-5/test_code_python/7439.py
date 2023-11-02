def solution():
    num_oranges = 96  # There are 96 oranges in total
    num_ripe = num_oranges / 2  # Half of the oranges are ripe
    num_unripe = num_oranges / 2  # Half of the oranges are unripe

    # Calculate how many ripe oranges were eaten
    num_ripe_eaten = num_ripe / 4  # 1/4 of the ripe oranges were eaten

    # Calculate how many unripe oranges were eaten
    num_unripe_eaten = num_unripe / 8  # 1/8 of the unripe oranges were eaten

    # Calculate how many oranges were left uneaten in total
    num_left = num_oranges - (num_ripe_eaten + num_unripe_eaten)

    result = num_left
    return result

print(solution())