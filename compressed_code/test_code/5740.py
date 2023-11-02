def solution():
    
    max_time = 30
    max_rate = 2
    max_filled = max_time * max_rate
    zach_time = 40
    zach_rate = 3
    zach_filled = zach_time * zach_rate
    total_filled = max_filled + zach_filled - 10
    result = total_filled
    return result

print(solution())