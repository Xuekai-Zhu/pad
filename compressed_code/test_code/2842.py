def solution():
    
    candy_bar_cost = 25
    chocolate_cost = 75
    juice_cost = 50
    num_candy_bars = 3
    num_chocolates = 2
    num_juices = 1

    total_cost = candy_bar_cost * num_candy_bars + chocolate_cost * num_chocolates + juice_cost * num_juices
    num_quarters = total_cost // 25  

    result = num_quarters
    return result

print(solution())