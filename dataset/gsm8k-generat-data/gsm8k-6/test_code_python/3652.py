def solution():
    # Calculate the total cost of the meals and sodas
    adult_meals = 6 * 6  # 6 adults at $6 each
    children_meals = 2 * 4  # 2 children at $4 each
    sodas = 8 * 2  # 8 people ordered sodas at $2 each
    total_cost = adult_meals + children_meals + sodas
    result = total_cost
    return result

print(solution())