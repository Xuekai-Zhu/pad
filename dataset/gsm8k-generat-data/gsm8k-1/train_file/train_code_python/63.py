def solution():
    """James earns $20 an hour while working at his main job. He earns 20% less while working his second job. He works 30 hours at his main job and half that much at his second job. How much does he earn per week?"""
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