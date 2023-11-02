def solution():
    """In the jar, there are 7 blue marbles, 11 red marbles, and some yellow marbles. If the chance of randomly picking a yellow marble is 1/4, how many yellow marbles are there?"""
    blue_marbles = 7
    red_marbles = 11
    total_marbles = blue_marbles + red_marbles + y  # let y be the number of yellow marbles
    prob_yellow = 1/4
    prob_of_picking_yellow = y / total_marbles
    prob_of_picking_yellow == prob_yellow  # setting the probabilities equal
    y = (prob_yellow * total_marbles) / 1  # solving for y
    result = y
    return result

print(solution())