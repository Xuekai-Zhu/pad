def solution():
    """James earns $20 an hour while working at his main job. He earns 20% less while working his second job. He works 30 hours at his main job and half that much at his second job. How much does he earn per week?"""
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