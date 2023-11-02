def solution():
    # Determine Allison's number of marbles
    allison_marbles = 28

    # Determine Angela's number of marbles
    angela_marbles = allison_marbles + 8

    # Determine Albert's number of marbles
    albert_marbles = 3 * angela_marbles

    # Determine total number of marbles Albert and Allison have
    total_marbles = albert_marbles + allison_marbles
    result = total_marbles
    return result

print(solution())