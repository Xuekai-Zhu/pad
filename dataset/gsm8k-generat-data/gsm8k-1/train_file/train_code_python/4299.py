def solution():
    """To finish the task assigned to her by the work supervisor in the stipulated deadline, Anie needs 5 hours extra aside from the normal work schedule each day. If each day her work schedule requires her to be productive for 10 hours, and the project is estimated to take 1500 hours, calculate the number of days it would take Anie to finish the job."""
    normal_work_hours = 10
    extra_hours = 5
    total_work_hours_per_day = normal_work_hours + extra_hours
    total_project_hours = 1500
    total_work_days = total_project_hours / total_work_hours_per_day
    result = total_work_days
    return result

print(solution())