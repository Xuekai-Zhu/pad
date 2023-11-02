def solution():
    rice_weight = 5  # Vicente bought 5 kilograms of rice
    meat_weight = 3  # Vicente bought 3 pounds of meat

    # Calculate the total cost of rice and meat
    rice_cost = rice_weight * 2  # $2 per kilogram of rice
    meat_cost = meat_weight * 5  # $5 per pound of meat
    total_cost = rice_cost + meat_cost
    result = total_cost
    return result

print(solution())