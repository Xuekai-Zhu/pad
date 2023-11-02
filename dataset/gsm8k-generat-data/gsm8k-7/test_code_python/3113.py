def solution():
    total_mangoes = 54
    ripe_mangoes = total_mangoes / 3
    unripe_mangoes = total_mangoes - ripe_mangoes

    # Subtract the 16 unripe mangoes that Jordan kept
    unripe_mangoes -= 16

    # Calculate the number of ripe mangoes that Jordan's sister received
    sister_mangoes = total_mangoes - unripe_mangoes

    # Calculate the number of jars of pickled mangoes Jordan's sister can make
    num_jars = sister_mangoes / 4
    result = num_jars
    return result

print(solution())