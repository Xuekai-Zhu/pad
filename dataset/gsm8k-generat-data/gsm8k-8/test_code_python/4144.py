def solution():
    total_money = 32
    bread_cost = 3
    candy_cost = 2
    money_left = total_money - bread_cost - candy_cost
    turkey_cost = money_left / 3
    money_left -= turkey_cost
    result = money_left
    return result

print(solution())