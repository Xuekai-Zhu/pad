def solution():
    # Calculate the cost of the steaks
    price_per_pound = 15
    pounds_bought = 20
    pounds_paid_for = pounds_bought / 2  # due to the buy one get one free offer
    cost = pounds_paid_for * price_per_pound
    result = cost
    return result

print(solution())