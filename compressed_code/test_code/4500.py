def solution():
    
    drips_per_minute = 10
    minutes_per_hour = 60
    drops_per_hour = drips_per_minute * minutes_per_hour
    volume_per_drop = 0.05
    total_volume = drops_per_hour * volume_per_drop
    result = total_volume
    return result

print(solution())