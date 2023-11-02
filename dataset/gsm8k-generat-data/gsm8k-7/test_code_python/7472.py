def solution():
    anika_age_ratio = 4/3
    maddie_age = 30 / anika_age_ratio
    average_age_after_15_years = (anika_age_ratio * (30 + 15) + maddie_age + 15) / 2
    result = average_age_after_15_years
    return result

print(solution())