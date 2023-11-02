def solution():
    # Calculate the number of clay pots made by the craftsman
    clay_pots = 16 / 2

    # Calculate the number of marbles in each clay pot
    clay_pot_marbles = 3 * 5

    # Calculate the total number of marbles
    total_marbles = 16 * 5 + clay_pots * clay_pot_marbles
    result = total_marbles
    return result

print(solution())