def solution():
    average_high_school_coach_salary = 41000
    ncsu_head_coach_salary = 1800000
    if average_high_school_coach_salary >= ncsu_head_coach_salary:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())