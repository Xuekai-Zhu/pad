def solution():
    """Paul has 52 marbles. His friend gave him 28 marbles. Then, he lost 1/4 of his marbles. How many marbles does Paul have left?"""
    starting_marbles = 52
    marbles_given = 28
    remaining_marbles = starting_marbles + marbles_given
    marbles_lost = starting_marbles / 4
    total_marbles = remaining_marbles - marbles_lost
    result = total_marbles
    return result

print(solution())