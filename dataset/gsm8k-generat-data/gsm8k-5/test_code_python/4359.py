def solution():
    total_time = 24  # There are 24 hours in a day
    sleeping_time = 1/3 * total_time  # Steve spends 1/3 of the day sleeping
    school_time = 1/6 * total_time  # Steve spends 1/6 of the day in school
    assignment_time = 1/12 * total_time  # Steve spends 1/12 of the day making assignments
    family_time = total_time - sleeping_time - school_time - assignment_time  # The remaining time is spent with family

    result = family_time
    return result

print(solution())