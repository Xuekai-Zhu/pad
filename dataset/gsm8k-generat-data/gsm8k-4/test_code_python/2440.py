def solution():
    """Wally gives 3/4 of his 400 tickets to his two friends Jensen and Finley, who share the tickets in a ratio of 4:11. How many tickets does Finley get?"""
    # Define the total number of tickets and the fraction given to friends
    total_tickets = 400
    fraction_given = 3/4

    # Calculate the number of tickets given to friends
    tickets_given = total_tickets * fraction_given

    # Define the ratio in which tickets are shared between Jensen and Finley
    jensen_ratio = 4
    finley_ratio = 11

    # Calculate the total ratio
    total_ratio = jensen_ratio + finley_ratio

    # Calculate the fraction of tickets given to Finley
    finley_fraction = finley_ratio / total_ratio

    # Calculate the number of tickets given to Finley
    finley_tickets = tickets_given * finley_fraction

    # Return the result
    result = finley_tickets
    return result

print(solution())