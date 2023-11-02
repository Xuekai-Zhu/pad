def solution():
    
    # Define the probability of winning for the first and second tickets
    probability_winning_1 = 0.2
    probability_winning_2 = 3 * probability_winning_1

    # Calculate the probability of winners for both tickets
    probability_winners_both = (probability_winning_1 + probability_winning_2) / 2

    # Convert the probability to a percentage
    probability_winners_percentage = probability_winners_both * 100

    # Display the probability winners percentage
    result = probability_winners_percentage
    return result

print(solution())