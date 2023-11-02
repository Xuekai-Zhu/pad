def solution():
    
    starting_money = 20
    candy_bar_cost = 2
    num_candy_bars = 4
    total_cost = candy_bar_cost * num_candy_bars
    remaining_money = starting_money - total_cost
    result = remaining_money
    return result

print(solution())