def solution():
    main_job_pay = 16 * 8 * 5  # Joanne earns $16 per hour, works 8 hours a day, and works 5 days a week at her main job
    part_time_job_pay = 13.5 * 2 * 5  # Joanne earns $13.5 per hour, works 2 hours a day, and works 5 days a week at her part-time job

    # Calculate Joanne's total earnings for the week
    total_earnings = main_job_pay + part_time_job_pay
    result = total_earnings
    return result

print(solution())