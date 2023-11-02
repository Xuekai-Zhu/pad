def solution():
    
    total_bars = 200
    bars_eaten = 80
    bars_remaining = total_bars - bars_eaten
    bars_per_child = 20
    num_children = bars_remaining // bars_per_child
    result = num_children
    return result

print(solution())