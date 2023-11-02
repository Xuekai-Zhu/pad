def solution():
    
    initial_money = 32
    bread_cost = 3
    candy_bar_cost = 2
    turkey_cost = (initial_money - bread_cost - candy_bar_cost) / 3
    remaining_money = initial_money - bread_cost - candy_bar_cost - turkey_cost
    result = remaining_money
    return result

print(solution())