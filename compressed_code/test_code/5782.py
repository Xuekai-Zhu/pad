def solution():
    
    wallet_cost = 100
    current_savings = wallet_cost / 2
    parents_money = 15
    grandparents_money = parents_money * 2
    total_money = current_savings + parents_money + grandparents_money
    money_needed = wallet_cost - total_money
    result = money_needed
    return result

print(solution())