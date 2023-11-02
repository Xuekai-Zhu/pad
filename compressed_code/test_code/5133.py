def solution():
    
    steps_per_km = 5350 / 3
    laps = 2.5
    total_distance = laps * 3
    total_steps = steps_per_km * total_distance
    result = total_steps
    return result

print(solution())