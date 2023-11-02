def solution():
    
    initial_racers = 50
    racers_joined = 30
    total_racers_20_min = initial_racers + racers_joined
    total_racers_50_min = total_racers_20_min * 2
    racers_dropped = total_racers_50_min - 130
    result = racers_dropped
    return result

print(solution())