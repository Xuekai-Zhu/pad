def solution():
    total_day = 24 # Total number of hours in a day
    sleep_time = total_day * (1/3) # Time spent sleeping
    school_time = total_day * (1/6) # Time spent in school
    assignment_time = total_day * (1/12) # Time spent making assignments
    total_time_spent = sleep_time + school_time + assignment_time
    family_time = total_day - total_time_spent # Time spent with family
    result = family_time
    return result

print(solution())