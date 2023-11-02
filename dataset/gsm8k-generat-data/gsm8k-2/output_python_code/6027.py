def solution():
    """Bethany loved riding horses. She rode 1 hour after school every Monday, Wednesday, and Friday. On Tuesday and Thursday, she rode for 30 min and on Saturdays, she could ride for 2 hours. How many hours in total did she ride over a 2 week period?"""
    num_weeks = 2
    num_days = 7
    num_mon_wed_fri = 3
    num_tue_thu = 2
    num_sat = 1
    time_mon_wed_fri = 1
    time_tue_thu = 0.5
    time_sat = 2
    total_time = (num_mon_wed_fri * time_mon_wed_fri + num_tue_thu * time_tue_thu + num_sat * time_sat) * num_weeks * num_days
    result = total_time
    return result

print(solution())