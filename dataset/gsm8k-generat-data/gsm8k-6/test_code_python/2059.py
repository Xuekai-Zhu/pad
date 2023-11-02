def solution():
    # Find the total number of marbles in the jar
    total_marbles = 7 + 11 + y  # let y be the number of yellow marbles

    # Set up an equation for the probability of picking a yellow marble
    yellow_probability = y/total_marbles

    # Solve for y using the given probability
    y = total_marbles/4 - 7 - 11
    result = y
    return result

print(solution())