def solution():
    
    total_meters = 30
    parts = 6
    used_parts = 4
    meters_per_part = total_meters / parts
    unused_meters = (parts - used_parts) * meters_per_part
    result = unused_meters
    return result

print(solution())