def solution():
    # Calculate how many tickets Wally gives away
    tickets_given_away = 3/4 * 400

    # Calculate the total ratio of tickets shared between Jensen and Finley
    total_ratio = 4 + 11

    # Calculate how many tickets Finley gets using their share of the ratio
    finley_tickets = (11/total_ratio) * tickets_given_away
    result = finley_tickets
    return result

print(solution())