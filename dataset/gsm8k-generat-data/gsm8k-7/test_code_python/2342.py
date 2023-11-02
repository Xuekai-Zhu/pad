def solution():
    monthly_rate = 50
    discount = 0.05
    num_months = 4

    regular_cost = monthly_rate * num_months

    discounted_cost = (monthly_rate * (1 - discount)) * num_months

    total_cost = regular_cost - discounted_cost
    result = total_cost
    return result

print(solution())