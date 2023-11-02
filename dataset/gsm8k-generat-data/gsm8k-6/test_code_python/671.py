def solution():
    # Calculate the number of ripe mangoes on the tree
    ripe_mangoes = (3/5) * 400  # 3/5 of 400 mangoes are ripe

    # Calculate the number of ripe mangoes Lindsay eats
    eaten_mangoes = 0.6 * ripe_mangoes  # Lindsay eats 60% of the ripe mangoes

    # Calculate the number of ripe mangoes remaining
    remaining_mangoes = ripe_mangoes - eaten_mangoes

    result = remaining_mangoes
    return result

print(solution())