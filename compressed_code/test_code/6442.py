def solution():
    
    actors_per_cycle = 5
    cycle_length_minutes = 15
    minutes_per_hour = 60
    cycles_per_hour = (minutes_per_hour // cycle_length_minutes)
    actors_per_hour = actors_per_cycle * cycles_per_hour
    result = actors_per_hour
    return result

print(solution())