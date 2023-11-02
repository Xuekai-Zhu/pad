def solution():
    
    main_job_rate = 16
    main_job_hours = 8
    part_time_rate = 13.5
    part_time_hours = 2
    days_per_week = 5
    total_main_job_pay = main_job_rate * main_job_hours * days_per_week
    total_part_time_pay = part_time_rate * part_time_hours * days_per_week
    total_pay = total_main_job_pay + total_part_time_pay
    result = total_pay
    return result

print(solution())