def solution():
    
    initial_money = 20
    socks_price = 2
    hat_price = 7
    socks_quantity = 4
    total_socks_price = socks_price * socks_quantity
    total_spent = total_socks_price + hat_price
    money_left = initial_money - total_spent
    result = money_left
    return result

print(solution())