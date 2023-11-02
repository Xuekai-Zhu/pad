def solution():
    
    toothbrush_per_patient = 2
    visit_time = 0.5
    work_days = 5
    work_hours_per_day = 8
    total_visits = work_days * work_hours_per_day * 2
    total_toothbrushes_given = total_visits * toothbrush_per_patient
    result = total_toothbrushes_given
    return result

print(solution())