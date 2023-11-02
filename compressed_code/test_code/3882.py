def solution():
    
    gift_money = 50
    novel_cost = 7
    lunch_cost = 2 * novel_cost
    total_spent = novel_cost + lunch_cost
    money_left = gift_money - total_spent
    result = money_left
    return result

print(solution())