def solution():
    annie_money = 120
    hamburgers = 8
    milkshakes = 6
    hamburger_price = 4
    milkshake_price = 3
    money_spent = (hamburgers * hamburger_price) + (milkshakes * milkshake_price)
    annie_money_left = annie_money - money_spent
    result = annie_money_left
    return result

print(solution())