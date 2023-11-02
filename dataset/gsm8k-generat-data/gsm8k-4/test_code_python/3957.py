def solution():
    """Joanne makes $16.00 working at her main job for 8 hours a day.  She has a part-time job, working an extra 2 hours a day where she makes $13.50 an hour.  How much money does she make if she works this schedule 5 days a week?"""
    # Calculate the total earnings from the main job
    main_job_earnings = 16 * 8 * 5

    # Calculate the total earnings from the part-time job
    part_time_earnings = 13.5 * 2 * 5

    # Calculate the total earnings from both jobs
    total_earnings = main_job_earnings + part_time_earnings

    # return the result
    result = total_earnings
    return result

print(solution())