def solution():
    skips_per_minute = 3 * 60 # 3 skips per second times 60 seconds in a minute
    minutes = 10
    total_skips = skips_per_minute * minutes
    result = total_skips
    return result

print(solution())