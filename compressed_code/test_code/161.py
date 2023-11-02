def solution():
    
    time_remaining = 5
    hotdogs_remaining = 75 - 20
    hotdogs_per_minute = hotdogs_remaining / time_remaining
    result = hotdogs_per_minute
    return result

print(solution())