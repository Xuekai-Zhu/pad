def solution():
    # Cost of clarinet lessons in a week
    cost_clarinet = 40 * 3  # $40 per hour, 3 hours per week

    # Cost of piano lessons in a week
    cost_piano = 28 * 5  # $28 per hour, 5 hours per week

    # Difference in cost between piano and clarinet lessons in a week
    difference_in_cost = cost_piano - cost_clarinet

    # Total cost difference in a year
    total_cost_difference = difference_in_cost * 52  # 52 weeks in a year

    result = total_cost_difference
    return result

print(solution())