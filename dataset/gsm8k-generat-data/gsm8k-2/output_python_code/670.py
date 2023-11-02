def solution():
    """3/5 of the mangoes on a mango tree are ripe. If Lindsay eats 60% of the ripe mangoes, calculate the number of ripe mangoes remaining if there were 400 mangoes on the tree to start with."""
    total_mangoes = 400
    ripe_mangoes = (3/5) * total_mangoes
    eaten_mangoes = 0.6 * ripe_mangoes
    remaining_mangoes = ripe_mangoes - eaten_mangoes
    result = remaining_mangoes
    return result

print(solution())