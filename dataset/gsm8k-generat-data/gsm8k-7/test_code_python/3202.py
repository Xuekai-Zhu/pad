def solution():
    old_babysitter_rate = 16
    new_babysitter_rate = 12
    extra_cost_per_scream = 3
    hours = 6
    screams = 2

    # Calculate the total cost of the old babysitter
    old_babysitter_cost = old_babysitter_rate * hours

    # Calculate the total cost of the new babysitter
    new_babysitter_cost = (new_babysitter_rate * hours) + (screams * extra_cost_per_scream)

    # Calculate the difference in cost between the two babysitters
    cost_difference = old_babysitter_cost - new_babysitter_cost
    result = cost_difference
    return result

print(solution())