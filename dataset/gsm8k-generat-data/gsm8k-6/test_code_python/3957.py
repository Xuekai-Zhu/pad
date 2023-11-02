def solution():
    # Calculate the total amount earned from the main job
    main_job_earnings = 16 * 8 * 5  # $16.00 working for 8 hours a day, 5 days a week

    # Calculate the total amount earned from the part-time job
    part_time_earnings = 13.5 * 2 * 5  # $13.50 an hour working for 2 hours a day, 5 days a week

    # Calculate the total amount earned for the week
    total_earnings = main_job_earnings + part_time_earnings

    result = total_earnings
    return result

print(solution())