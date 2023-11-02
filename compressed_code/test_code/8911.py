def solution():
    
    main_job_pay_rate = 16
    main_job_hours = 8
    
    part_time_job_pay_rate = 13.5
    part_time_job_hours = 2
    
    days_per_week = 5
    
    main_job_weekly_pay = main_job_pay_rate * main_job_hours * days_per_week
    part_time_job_weekly_pay = part_time_job_pay_rate * part_time_job_hours * days_per_week
    
    result = main_job_weekly_pay + part_time_job_weekly_pay
    
    return result

print(solution())