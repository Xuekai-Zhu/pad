def solution():
    """Roberto can skip 4,200 times an hour. Valerie can skip 80 times a minute. If they jump rope for fifteen minutes straight, how many skips will they total?"""
    roberto_skips_per_min = 4200 / 60
    valerie_skips_per_min = 80
    total_mins = 15
    roberto_skips = roberto_skips_per_min * total_mins
    valerie_skips = valerie_skips_per_min * total_mins
    total_skips = roberto_skips + valerie_skips
    result = total_skips
    return result

print(solution())