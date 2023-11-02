def solution():
    # Calculate James' earnings from his main job
    main_job_earnings = 20 * 30  # $20 an hour, 30 hours of work
    
    # Calculate James' earnings from his second job
    second_job_earnings_per_hour = 0.8 * 20  # 20% less than his main job hourly rate
    second_job_hours = 30/2  # half as much work as his main job
    second_job_earnings = second_job_earnings_per_hour * second_job_hours
    
    # Calculate James' total weekly earnings
    total_earnings = main_job_earnings + second_job_earnings
    result = total_earnings
    return result

print(solution())