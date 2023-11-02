def solution():
    num_shots_per_week = 200 * 4
    recovery_rate = 0.2
    arrow_cost = 5.5
    team_coverage = 0.7

    # Calculate the total number of arrows used by the archer
    total_arrows_used = num_shots_per_week * (1 - recovery_rate)

    # Calculate the total cost of all arrows before team coverage
    total_cost_before_coverage = total_arrows_used * arrow_cost

    # Calculate the total cost of all arrows after team coverage
    total_cost_after_coverage = total_cost_before_coverage * (1 - team_coverage)

    result = total_cost_after_coverage
    return result

print(solution())