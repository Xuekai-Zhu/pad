def solution():
    initial_day = 10
    increase_per_day = 4
    days_per_week = 6
    cost_per_candy_bar = 0.1
    total_candy_bars = initial_day + ((increase_per_day * days_per_week) - increase_per_day)
    total_cost = total_candy_bars * cost_per_candy_bar
    result = total_cost
    return result

print(solution())