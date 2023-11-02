def solution():
    # Calculate the cost of the first babysitter
    first_babysitter_cost = 16 * 6

    # Calculate the cost of the new babysitter without screaming fees
    new_babysitter_cost = 12 * 6

    # Calculate the cost of the new babysitter's screaming fees
    new_babysitter_scream_fees = 2 * 3

    # Calculate the total cost of the new babysitter
    new_babysitter_total_cost = new_babysitter_cost + new_babysitter_scream_fees

    # Calculate the difference in cost between the two babysitters
    cost_difference = first_babysitter_cost - new_babysitter_total_cost

    result = cost_difference
    return result

print(solution())