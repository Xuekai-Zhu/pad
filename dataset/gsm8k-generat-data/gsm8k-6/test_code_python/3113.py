def solution():
    # Find the number of ripe mangoes
    ripe_mangoes = 54 / 3

    # Find the number of unripe mangoes Jordan gave to his sister
    unripe_mangoes = (2/3) * 54 - 16

    # Calculate the number of jars of pickled mangoes Jordan's sister can make
    jars = unripe_mangoes // 4

    result = jars
    return result

print(solution())