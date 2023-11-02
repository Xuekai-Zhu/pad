def solution():
    main_job_pay = 16.0
    main_job_hours = 8
    part_time_pay = 13.5
    part_time_hours = 2
    work_days = 5

    # Calculate the total pay for the main job
    main_job_total_pay = main_job_pay * main_job_hours * work_days

    # Calculate the total pay for the part-time job
    part_time_total_pay = part_time_pay * part_time_hours * work_days

    # Calculate the total pay for both jobs
    total_pay = main_job_total_pay + part_time_total_pay
    result = total_pay
    return result

print(solution())