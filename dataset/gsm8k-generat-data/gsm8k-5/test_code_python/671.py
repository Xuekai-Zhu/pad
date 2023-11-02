def solution():
    total_mangoes = 400  # There were 400 mangoes on the tree to start with
    ripe_mangoes = 3/5 * total_mangoes  # 3/5 of the mangoes on the tree are ripe
    eaten_mangoes = 0.6 * ripe_mangoes  # Lindsay eats 60% of the ripe mangoes
    remaining_mangoes = ripe_mangoes - eaten_mangoes  # Calculate the number of ripe mangoes remaining

    result = remaining_mangoes
    return result

print(solution())