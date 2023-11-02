def solution():
    
    total_days = 30
    remaining_days = total_days - (4/5 * total_days)
    remaining_pills = 12
    pills_per_day = remaining_pills / remaining_days
    result = pills_per_day
    return result

print(solution())