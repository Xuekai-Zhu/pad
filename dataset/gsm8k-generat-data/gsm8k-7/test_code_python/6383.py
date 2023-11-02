def solution():
    beef_weight = 4
    veggie_weight = 6

    veggie_price_per_pound = 2
    beef_price_per_pound = 3 * veggie_price_per_pound

    # Calculate the total cost of vegetables
    veggie_cost = veggie_weight * veggie_price_per_pound

    # Calculate the total cost of beef
    beef_cost = beef_weight * beef_price_per_pound

    # Calculate the total cost of everything
    total_cost = veggie_cost + beef_cost
    result = total_cost
    return result

print(solution())