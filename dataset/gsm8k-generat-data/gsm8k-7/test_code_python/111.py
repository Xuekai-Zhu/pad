def solution():
    bread_price = 2
    butter_price = 3
    juice_price = 2 * bread_price
    total_cost = bread_price + butter_price + juice_price
    money_left = 15 - total_cost
    result = money_left
    return result

print(solution())