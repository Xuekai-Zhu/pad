def solution():
    rolls_per_day = 1
    days_per_week = 7
    weeks = 4
    rolls_needed = rolls_per_day * days_per_week * weeks
    packs_needed = rolls_needed / 12
    result = packs_needed
    return result

print(solution())