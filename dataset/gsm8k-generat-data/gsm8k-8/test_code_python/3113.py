def solution():
    # Calculate the number of ripe mangoes
    ripe_mangoes = 54 / 3

    # Calculate the number of unripe mangoes Jordan kept
    unripe_mangoes = 54 - ripe_mangoes - 16

    # Calculate the number of mangoes left for Jordan's sister
    remaining_mangoes = ripe_mangoes + unripe_mangoes

    # Calculate the number of jars Jordan's sister can make
    jars = remaining_mangoes // 4
    result = jars
    return result

print(solution())