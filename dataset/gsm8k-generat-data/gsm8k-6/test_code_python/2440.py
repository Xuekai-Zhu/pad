def solution():
    # Find the total number of tickets Wally gives to his friends
    friends_tickets = (3/4) * 400  

    # Find the total ratio of Jensen and Finley's tickets
    total_ratio = 4 + 11  

    # Find Finley's share of the tickets using the ratio of her tickets to the total ratio
    finley_tickets = (11/total_ratio) * friends_tickets
    result = finley_tickets
    return result

print(solution())