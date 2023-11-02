def solution():
    food_cost = 50
    service_fee = 0.12  # 12% service fee
    tip = 5

    # Calculate the cost of the service fee
    service_fee_cost = food_cost * service_fee

    # Calculate the total cost of the meal
    total_cost = food_cost + service_fee_cost + tip
    result = total_cost
    return result

print(solution())