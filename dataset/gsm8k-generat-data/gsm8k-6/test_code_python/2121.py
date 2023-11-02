def solution():
    # Calculate the cost per batch of peanut butter cookies
    peanut_butter_cost = 3  # cost of a jar of peanut butter
    peanut_butter_batch_cost = peanut_butter_cost / 2  # cost of half a jar of peanut butter per batch

    # Calculate the cost per batch of almond butter cookies
    almond_butter_cost = 3 * peanut_butter_cost  # cost of a jar of almond butter
    almond_butter_batch_cost = almond_butter_cost / 2  # cost of half a jar of almond butter per batch

    # Calculate the difference in cost per batch
    cost_difference = almond_butter_batch_cost - peanut_butter_batch_cost
    result = cost_difference
    return result

print(solution())