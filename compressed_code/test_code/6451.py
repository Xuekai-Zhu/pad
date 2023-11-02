def solution():
    
    daily_run_time = 60
    weekdays = 5
    thursday_reduction = 20
    friday_increase = 10
    total_run_time = daily_run_time * weekdays - thursday_reduction + friday_increase
    result = total_run_time
    return result

print(solution())