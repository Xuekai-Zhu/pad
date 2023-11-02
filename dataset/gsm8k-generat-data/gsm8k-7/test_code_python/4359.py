def solution():
    total_day = 24 # in hours
    sleeping_time = total_day * (1/3)
    school_time = total_day * (1/6)
    assignment_time = total_day * (1/12)
    family_time = total_day - sleeping_time - school_time - assignment_time 
    result = family_time
    return result

print(solution())