def solution():
    international_cost_per_day = 3.50
    num_days_in_december = 10
    regular_plan_cost_per_month = 175

    # Calculate the total cost of the international data usage
    international_cost = international_cost_per_day * num_days_in_december

    # Add the regular plan cost to the international data cost
    total_cost = regular_plan_cost_per_month + international_cost
    result = total_cost
    return result

print(solution())