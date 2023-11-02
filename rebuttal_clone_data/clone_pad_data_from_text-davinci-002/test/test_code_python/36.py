def solution():
    
    main_job_hourly_rate = 20
    second_job_hourly_rate = main_job_hourly_rate * 0.8
    main_job_hours_worked = 30
    second_job_hours_worked = main_job_hours_worked / 2
    main_job_weekly_earnings = main_job_hourly_rate * main_job_hours_worked
    second_job_weekly_earnings = second_job_hourly_rate * second_job_hours_worked
    total_weekly_earnings = main_job_weekly_earnings + second_job_weekly_earnings
    result = total_weekly_earnings
    return result

print(solution())