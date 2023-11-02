def solution():
    age_limit = 35
    eleventh_grade_age_range = range(16, 18)
    if max(eleventh_grade_age_range) < age_limit:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())