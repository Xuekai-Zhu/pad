def solution():
    
    monday_study_time = 4
    tuesday_study_time = 2 * monday_study_time
    wednesday_study_time = 3
    thursday_study_time = 3
    friday_study_time = 3
    total_study_time = monday_study_time + tuesday_study_time + wednesday_study_time + thursday_study_time + friday_study_time
    remaining_study_time = 25 - total_study_time
    saturday_study_time = remaining_study_time / 2
    result = saturday_study_time
    return result

print(solution())