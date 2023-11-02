def solution():
    # Find the number of clay pots made
    pots_made = 16 / 2

    # Calculate the number of marbles in each jar
    marbles_per_jar = 5

    # Calculate the number of marbles in each clay pot
    marbles_per_pot = 3 * marbles_per_jar

    # Calculate the total number of marbles
    total_marbles = (pots_made * marbles_per_pot) + (16 * marbles_per_jar)

    result = total_marbles
    return result

print(solution())