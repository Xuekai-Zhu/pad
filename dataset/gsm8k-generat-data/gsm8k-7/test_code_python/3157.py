def solution():
    base_cost = 45.0
    max_gb = 100
    overage_rate = 0.25
    total_cost = 65.0

    # Calculate the cost of the base plan without any overage charges
    base_plan_cost = base_cost

    # Calculate the remaining amount of money available for overage charges
    overage_budget = total_cost - base_plan_cost

    # Calculate the maximum amount of GB that can be used within the budget for overage charges
    max_overage_gb = overage_budget / overage_rate

    # Calculate the actual amount of GB used beyond the base plan
    actual_overage_gb = max(0, max_overage_gb - max_gb)

    result = actual_overage_gb
    return result

print(solution())