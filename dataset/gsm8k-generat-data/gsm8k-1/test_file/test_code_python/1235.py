def solution():
    """A custodian has to clean a school with 80 classrooms. They have 5 days to get it done. It takes them 15 minutes per classroom. If they work an 8 hour day, what percentage of their day, on average, is spent cleaning classrooms?"""
    num_classrooms = 80
    num_days = 5
    clean_time_min = num_classrooms * 15
    clean_time_hr = clean_time_min / 60
    work_time_hr = num_days * 8
    percent_cleaning = (clean_time_hr / work_time_hr) * 100
    result = percent_cleaning
    return result

print(solution())