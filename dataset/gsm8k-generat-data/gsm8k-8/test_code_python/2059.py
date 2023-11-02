def solution():
    # Calculate the total number of marbles
    total_marbles = 7 + 11

    # Calculate the probability of picking a yellow marble
    yellow_probability = 1/4

    # Solve for the number of yellow marbles
    yellow_marbles = (yellow_probability * (total_marbles + x)) - total_marbles

    result = yellow_marbles
    return result

print(solution())