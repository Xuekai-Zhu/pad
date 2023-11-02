def solution():
    cheese_cost = 4  # $4 per kg of cheese
    vegetable_cost = cheese_cost + 2  # $2 more expensive than the cost of 1 kg of cheese
    cheese_weight = 8  # Emma bought 8 kg of cheese
    vegetable_weight = 7  # Emma bought 7 kg of vegetables

    # Calculate the total cost of cheese
    cheese_total_cost = cheese_cost * cheese_weight

    # Calculate the total cost of vegetables
    vegetable_total_cost = vegetable_cost * vegetable_weight

    # Calculate the total cost of Emma's shopping
    total_cost = cheese_total_cost + vegetable_total_cost
    result = total_cost
    return result

print(solution())