def solution():
    num_jars = 16
    num_pots = num_jars / 2
    marbles_per_jar = 5
    marbles_per_pot = 3 * marbles_per_jar

    # Calculate the total number of marbles from jars
    total_jar_marbles = num_jars * marbles_per_jar

    # Calculate the total number of marbles from pots
    total_pot_marbles = num_pots * marbles_per_pot

    # Calculate the overall total number of marbles
    total_marbles = total_jar_marbles + total_pot_marbles
    result = total_marbles
    return result

print(solution())