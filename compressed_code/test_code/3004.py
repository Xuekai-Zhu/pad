def solution():
    
    initial_money = 20
    added_money = 2 * initial_money
    total_money = initial_money + added_money
    cupcakes_cost = 10 * 1.5
    cookies_cost = 5 * 3
    total_cost = cupcakes_cost + cookies_cost
    money_left = total_money - total_cost
    result = money_left
    return result

print(solution())