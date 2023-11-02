def solution():
    """Three friends went out to watch a movie. Mitch paid for their tickets at $7 each. On the other hand, Jam paid for the 2 boxes of popcorn at $1.5 while Jay paid for the 3 cups of milk tea at $3 each. If the three of them will split the total expenses, how much should each contribute?"""
    ticket_cost = 7
    popcorn_cost = 1.5 * 2
    tea_cost = 3 * 3
    total_cost = ticket_cost + popcorn_cost + tea_cost
    num_friends = 3
    each_contribution = total_cost / num_friends
    result = each_contribution
    return result

print(solution())