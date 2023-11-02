def solution():
    
    total_students = 30
    valentines_percent = 0.6
    valentines_to_buy = int(total_students * valentines_percent)
    valentine_cost = 2
    total_cost = valentines_to_buy * valentine_cost
    money_spent_percent = (total_cost / 40) * 100
    result = money_spent_percent
    return result

print(solution())