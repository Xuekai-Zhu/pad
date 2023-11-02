def solution():
    # Define initial number of marbles
    initial_marbles = 26

    # Find number of marbles Hilton has after finding 6 and losing 10
    current_marbles = initial_marbles + 6 - 10

    # Find number of marbles Lori gave Hilton
    lori_gave = 2 * 10

    # Find final number of marbles
    final_marbles = current_marbles + lori_gave

    result = final_marbles
    return result

print(solution())