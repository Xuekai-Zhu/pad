def solution():
    """Jack is a soccer player. He needs to buy two pairs of socks and a pair of soccer shoes. Each pair of socks cost $9.50, and the shoes cost $92. Jack has $40. How much more money does Jack need?"""
    socks_price = 9.5
    shoes_price = 92
    num_socks = 2

    total_cost = (socks_price * num_socks) + shoes_price
    remaining_money = 40 - total_cost
    result = abs(remaining_money)
    return result

print(solution())