def solution():
    heating_pad_cost = 30
    num_uses_per_week = 3
    num_weeks = 2

    # Calculate the total number of uses
    total_uses = num_uses_per_week * num_weeks

    # Calculate the cost per use
    cost_per_use = heating_pad_cost / total_uses
    result = cost_per_use
    return result

print(solution())