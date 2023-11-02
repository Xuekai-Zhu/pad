def solution():
    
    drops_per_minute = 3
    ml_per_drop = 20
    liters_in_pot = 3
    ml_in_pot = liters_in_pot * 1000
    drops_needed = ml_in_pot / ml_per_drop
    time_to_fill = drops_needed / drops_per_minute
    result = time_to_fill
    
    return result

print(solution())