def solution():
    starting_marbles = 26
    found_marbles = 6
    lost_marbles = 10
    given_marbles = 2 * lost_marbles

    # Calculate the total number of marbles Hilton has after finding and losing marbles
    total_marbles = starting_marbles + found_marbles - lost_marbles

    # Add the marbles given by Lori
    total_marbles += given_marbles
    result = total_marbles
    return result

print(solution())