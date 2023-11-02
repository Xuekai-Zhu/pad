def solution():
    sock_cost = 2
    sock_profit = 0.25
    socks_bought = 9
    socks_resold = 4
    socks_sold_for_profit = socks_bought - socks_resold
    total_profit = (socks_resold * (sock_cost * sock_profit)) + (socks_sold_for_profit * 0.2)
    result = total_profit
    return result

print(solution())