def solution():
    chicken_weight = 2
    beef_weight = 3
    beef_price_per_pound = 4
    oil_price = 1
    total_cost = 16

    # Calculate the total cost of the chicken
    chicken_cost = total_cost - (beef_weight * beef_price_per_pound) - oil_price

    # Calculate the cost for each person if divided evenly
    cost_per_person = chicken_cost / 3

    # Calculate the cost per pound of chicken
    cost_per_pound = cost_per_person / chicken_weight
    result = cost_per_pound
    return result

print(solution())