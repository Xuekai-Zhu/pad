def solution():
    
    hose_capacity = 20
    total_water_needed = 4000
    firefighters = 5
    total_hoses = firefighters
    total_water_per_minute = hose_capacity * total_hoses
    time_to_put_out_fire = total_water_needed / total_water_per_minute
    result = time_to_put_out_fire
    return result

print(solution())