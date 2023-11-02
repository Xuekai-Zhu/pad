def solution():
    original_cost = 200
    new_capacity = 2
    price_increase = 0.2  # 20% increase

    # Calculate the new cost per gallon
    new_cost = original_cost / (new_capacity * (1 + price_increase))

    result = new_cost
    return result

print(solution())