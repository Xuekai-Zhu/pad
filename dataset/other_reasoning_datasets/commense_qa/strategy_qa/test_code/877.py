def solution():
    eleventh_grade_age = 16
    medicare_age_requirement = 65
    if eleventh_grade_age < medicare_age_requirement:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())