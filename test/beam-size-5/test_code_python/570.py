def solution():
    
    bread_price = 3.00
    sandwiches_per_loaf = 10
    cheeses_cost = 30.00
    condiments_per_sandwich = 10
    sandwich_price = 7.00
    total_sandwiches = sandwiches_per_loaf * sandwiches_per_loaf
    total_cost = total_sandwiches * cheeses_cost + condiments_per_sandwich * sandwich_price
    net_profit = total_cost - bread_price
    result = net_profit
    return result

print(solution())