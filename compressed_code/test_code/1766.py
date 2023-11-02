def solution():
    
    initial_racers = 50
    new_racers_after_20_minutes = 30
    total_racers_after_20_minutes = initial_racers + new_racers_after_20_minutes
    total_racers_after_50_minutes = total_racers_after_20_minutes * 2
    racers_who_finished = 130
    racers_who_dropped = total_racers_after_50_minutes - racers_who_finished
    result = racers_who_dropped
    return result

print(solution())