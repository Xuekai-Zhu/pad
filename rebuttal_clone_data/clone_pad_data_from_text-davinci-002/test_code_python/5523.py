def solution():
    cash_on_hand = 240
    monthly_cost = 50
    sale_price = 30
    months = 0

    while cash_on_hand >= monthly_cost:
        cash_on_hand -= monthly_cost
        cash_on_hand += sale_price
        months += 1

    return months

print(solution())