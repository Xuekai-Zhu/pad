def solution():
    """Penny has $20. Penny buys 4 pairs of socks for $2 a pair and a hat for $7. How much money does Penny have left?"""
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