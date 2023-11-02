def solution():
    borrowed_money = 20 + 40 + 30
    gifted_money = 70
    savings = 100
    total_money = borrowed_money + gifted_money + savings
    money_spent = total_money * (3/4)
    money_left = total_money - money_spent
    result = money_left
    return result

print(solution())