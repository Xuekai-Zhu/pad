def solution():
    
    total_bars = 200
    bars_eaten = 80
    bars_left = total_bars - bars_eaten
    child_bars = 20
    num_children = bars_left / child_bars
    result = num_children
    return result

print(solution())