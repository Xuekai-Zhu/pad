def solution():
    # Calculate the cost of the original babysitter
    original_cost = 16 * 6  # $16/hour for 6 hours

    # Calculate the cost of the new babysitter
    new_cost = 12 * 6 + 3 * 2  # $12/hour for 6 hours + $3 per scream, twice per babysitting gig

    # Calculate the difference in cost
    cost_difference = original_cost - new_cost
    result = cost_difference
    return result

print(solution())