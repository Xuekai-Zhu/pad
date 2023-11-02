def solution():
    
    socks_price = 9.5
    shoes_price = 92
    num_socks = 2

    total_cost = (socks_price * num_socks) + shoes_price
    remaining_money = 40 - total_cost
    result = abs(remaining_money)
    return result

print(solution())