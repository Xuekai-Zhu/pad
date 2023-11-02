def solution():
    """A craftsman makes 16 jars. This is exactly twice the number of clay pots he made. If each jar has 5 marbles and each clay pot has three times as many, how many marbles are there?"""
    num_jars = 16
    num_pots = num_jars / 2
    jar_marbles = 5
    pot_marbles = 3 * jar_marbles

    total_jar_marbles = num_jars * jar_marbles
    total_pot_marbles = num_pots * pot_marbles
    total_marbles = total_jar_marbles + total_pot_marbles

    result = total_marbles
    return result

print(solution())