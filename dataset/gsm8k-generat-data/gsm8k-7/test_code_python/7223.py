def solution():
    amount_of_meat = 2
    cost_per_kg = 82
    total_cost = amount_of_meat * cost_per_kg
    wallet_amount = 180

    # Calculate the amount of money Méliès will have left after paying for the meat
    money_left = wallet_amount - total_cost
    result = money_left
    return result

print(solution())