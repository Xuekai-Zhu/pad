def solution():
    # Calculate the total number of marbles Courtney has
    jar1 = 80  # number of marbles in the first jar
    jar2 = 2 * jar1  # number of marbles in the second jar
    jar3 = jar1 / 4  # number of marbles in the third jar
    total_marbles = jar1 + jar2 + jar3
    result = total_marbles
    return result

print(solution())