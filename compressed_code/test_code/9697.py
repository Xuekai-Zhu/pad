def solution():
    
    lee_money = 10
    friend_money = 8
    cost_of_food = 6 + 4 + 1 + 1
    tax = 3
    total_cost = cost_of_food + tax
    money_paid = lee_money + friend_money
    change = money_paid - total_cost
    result = change
    return result

print(solution())