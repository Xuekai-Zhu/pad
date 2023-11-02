def solution():
    wallet_cost = 100
    saved_money = wallet_cost / 2
    parents_money = 15
    grandparents_money = 2 * parents_money
    total_money = saved_money + parents_money + grandparents_money
    money_needed = wallet_cost - total_money
    result = money_needed
    return result

print(solution())