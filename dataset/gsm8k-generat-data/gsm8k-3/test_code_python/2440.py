def solution():
    """Wally gives 3/4 of his 400 tickets to his two friends Jensen and Finley, who share the tickets in a ratio of 4:11. How many tickets does Finley get?"""
    # Calculate the number of tickets Wally gives away
    tickets_given_away = 3/4 * 400

    # Calculate the total ratio of tickets shared by Jensen and Finley
    total_ratio = 4 + 11

    # Calculate the fraction of tickets Finley gets
    finley_ratio = 11/total_ratio

    # Calculate the number of tickets Finley gets
    finley_tickets = tickets_given_away * finley_ratio

    # Display the number of tickets Finley gets
    result = finley_tickets
    return result

print(solution())