def solution():
    loaves_per_hour = 10
    baguettes_per_two_hours = 30
    hours_baked_per_day = 6
    total_loaves = loaves_per_hour * hours_baked_per_day + (baguettes_per_two_hours / 2) * hours_baked_per_day
    result = total_loaves
    return result

print(solution())