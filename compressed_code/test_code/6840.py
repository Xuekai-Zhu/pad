def solution():
    
    max_riding_time = 6
    half_max_riding_time = max_riding_time / 2
    days_at_max = 2
    days_at_half = 2
    days_at_1_5 = 2
    total_time = (max_riding_time * days_at_max) + (half_max_riding_time * days_at_half) + (1.5 * days_at_1_5)
    result = total_time
    return result

print(solution())