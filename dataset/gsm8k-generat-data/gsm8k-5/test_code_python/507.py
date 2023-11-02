def solution():
    price_per_pound = 15  # James pays $15 per pound
    pounds_bought = 20  # James buys 20 pounds of steaks
    pounds_paid_for = pounds_bought / 2  # James only pays for half the amount of steaks he buys

    # Calculate the total amount James pays for the steaks
    total_price = pounds_paid_for * price_per_pound
    result = total_price
    return result

print(solution())