def solution():
    """Abigail spent 60% of her money on food, and 25% of the remainder on her phone bill. After spending $20 on entertainment, she is left with $40. How much money did Abigail have initially?"""
    remaining_money_after_food = 40 / (1 - 0.6)
    phone_bill_money = 0.25 * (remaining_money_after_food - 20)
    initial_money = remaining_money_after_food - phone_bill_money - 20
    result = initial_money
    return result

print(solution())