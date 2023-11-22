def solution():
    
    # Define the probability of winning a lottery ticket
    winning_1 = 0.2

    # Define the probability of winning a lottery ticket that's three times more likely to win
    winning_2 = 3 * winning_1

    # Calculate the probability of winning both tickets
    winning_total = winning_1 + winning_2

    # Convert the probability to a percentage
    winning_percentage = winning_total * 100

    # Display the probability as a percentage
    result = winning_percentage
    return result

print(solution())