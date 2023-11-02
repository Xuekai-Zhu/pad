def solution():
    jars = 16
    pots = jars / 2  # The craftsman made half the number of pots as jars

    # Calculate the total number of marbles in the jars
    jar_marbles = jars * 5

    # Calculate the total number of marbles in the clay pots
    pot_marbles = pots * 3 * 5  # Each pot contains three times as many marbles as a jar

    # Calculate the total number of marbles
    total_marbles = jar_marbles + pot_marbles
    result = total_marbles
    return result

print(solution())