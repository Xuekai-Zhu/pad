def solution():
    """Roberto can skip 4,200 times an hour. Valerie can skip 80 times a minute. If they jump rope for fifteen minutes straight, how many skips will they total?"""
    roberto_skips_per_minute = 4200 / 60
    valerie_skips_per_minute = 80
    total_skips_per_minute = roberto_skips_per_minute + valerie_skips_per_minute
    total_skips = total_skips_per_minute * 15
    result = total_skips
    return result

print(solution())