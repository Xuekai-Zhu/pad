def solution():
    
    bread_price = 2
    butter_price = 3
    juice_price = 2 * bread_price
    total_price = bread_price + butter_price + juice_price
    money_left = 15 - total_price
    result = money_left
    return result

print(solution())