def solution():
    normal_work_hours = 10  # Anie's work schedule requires her to work for 10 hours a day
    extra_hours = 5  # Anie needs to work an extra 5 hours each day to meet the deadline
    total_work_hours = normal_work_hours + extra_hours  # Total hours Anie works each day
    total_project_hours = 1500  # Estimated total time to complete the project

    # Calculate the total number of days required to finish the job
    total_days = total_project_hours / total_work_hours

    result = total_days
    return result

print(solution())