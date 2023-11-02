def solution():
    
    skips_per_second = 3
    jumps_per_minute = skips_per_second * 60
    duration_in_minutes = 10
    total_jumps = jumps_per_minute * duration_in_minutes
    result = total_jumps
    return result

print(solution())