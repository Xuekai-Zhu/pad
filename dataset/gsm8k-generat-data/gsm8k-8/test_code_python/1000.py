def solution():
    # Define the variables
    cost = 30
    uses_per_week = 3
    weeks_of_use = 2

    # Calculate the total number of uses
    total_uses = uses_per_week * weeks_of_use

    # Calculate the cost per use
    cost_per_use = cost / total_uses
    result = cost_per_use
    return result

print(solution())