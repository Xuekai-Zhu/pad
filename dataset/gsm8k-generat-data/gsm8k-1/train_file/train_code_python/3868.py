def solution():
    """Tom hasn't been sleeping well lately. He figures he has been getting about 5 hours of sleep each weeknight and 6 hours each night on the weekend. If Tom would ideally like to get 8 hours of sleep each night on both weeknights and weekends, how many hours of sleep is Tom behind on from the last week?"""
    ideal_weekday_hours = 8
    ideal_weekend_hours = 8
    actual_weekday_hours = 5
    actual_weekend_hours = 6
    weekday_hours_behind = ideal_weekday_hours - actual_weekday_hours
    weekend_hours_behind = ideal_weekend_hours - actual_weekend_hours
    total_hours_behind = (weekday_hours_behind * 5) + (weekend_hours_behind * 2)
    result = total_hours_behind
    return result

print(solution())