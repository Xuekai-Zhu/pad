def solution():
    
    main_job_hourly_pay = 20
    second_job_hourly_pay = main_job_hourly_pay * 0.8
    main_job_hours = 30
    second_job_hours = main_job_hours / 2
    main_job_earnings = main_job_hourly_pay * main_job_hours
    second_job_earnings = second_job_hourly_pay * second_job_hours
    total_earnings = main_job_earnings + second_job_earnings
    result = total_earnings
    return result

print(solution())