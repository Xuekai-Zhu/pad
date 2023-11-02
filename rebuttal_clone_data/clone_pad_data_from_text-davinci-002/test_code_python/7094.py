def solution():
    age_start = 13
    age_end = 16
    miles_ridden_per_day = 3
    total_miles_ridden = (age_end - age_start) * miles_ridden_per_day * 365
    result = total_miles_ridden
    return result

print(solution())