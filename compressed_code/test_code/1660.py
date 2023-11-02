def solution():
    
    driving_time_per_day = 2 * 20 / 60 
    total_driving_time_required = 50
    school_days_required = total_driving_time_required / driving_time_per_day
    result = school_days_required
    return result

print(solution())