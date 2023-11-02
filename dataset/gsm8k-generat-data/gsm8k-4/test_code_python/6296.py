def solution():
    """A craftsman makes 16 jars. This is exactly twice the number of clay pots he made. If each jar has 5 marbles and each clay pot has three times as many, how many marbles are there?"""
    # Calculate the number of clay pots made
    clay_pots = 16 / 2

    # Calculate the number of marbles in each clay pot
    clay_pot_marbles = 3 * 5

    # Calculate the total number of marbles in the clay pots
    total_clay_pot_marbles = clay_pots * clay_pot_marbles

    # Calculate the total number of marbles in the jars
    jar_marbles = 16 * 5

    # Calculate the total number of marbles
    total_marbles = total_clay_pot_marbles + jar_marbles

    # return the result
    result = total_marbles
    return result

print(solution())