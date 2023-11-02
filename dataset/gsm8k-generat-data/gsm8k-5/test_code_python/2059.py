def solution():
    total_marbles = 7 + 11  # Total number of marbles in the jar
    probability_yellow = 1/4  # The probability of picking a yellow marble
    probability_not_yellow = 1 - probability_yellow  # The probability of not picking a yellow marble
    
    # We can use the ratio of probabilities to find the number of yellow marbles
    ratio = probability_yellow / probability_not_yellow
    yellow_marbles = ratio * total_marbles - 7 - 11  # Subtract the number of blue and red marbles
    
    result = yellow_marbles
    return result

print(solution())