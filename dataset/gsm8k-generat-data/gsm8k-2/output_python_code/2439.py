def solution():
    """Wally gives 3/4 of his 400 tickets to his two friends Jensen and Finley, who share the tickets in a ratio of 4:11. How many tickets does Finley get?"""
    wally_tickets = 400 * (3/4)
    total_ratio = 4 + 11
    finley_ratio = 11 / total_ratio
    finley_tickets = finley_ratio * wally_tickets
    result = finley_tickets
    return result

print(solution())