def solution():
    # Calculate total number of marbles
    total_marbles = 12 + 28

    # Calculate the number of marbles each person takes away
    marbles_taken = (1/4) * total_marbles

    # Calculate the number of marbles remaining in the pile
    remaining_marbles = total_marbles - (2 * marbles_taken)

    result = remaining_marbles
    return result

print(solution())