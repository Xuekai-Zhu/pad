def solution():
    # Define the number of original marbles and the number lost
    original_marbles = 12
    lost_marbles = original_marbles / 2

    # Calculate the number of marbles left after the loss
    marbles_left = original_marbles - lost_marbles

    # Add 10 more marbles and the new bag of marbles
    total_marbles = marbles_left + 10 + 25
    result = total_marbles
    return result

print(solution())