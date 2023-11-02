def solution():
    """Joanne makes $16.00 working at her main job for 8 hours a day. She has a part-time job, working an extra 2 hours a day where she makes $13.50 an hour. How much money does she make if she works this schedule 5 days a week?"""
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