def solution():
    """To finish the task assigned to her by the work supervisor in the stipulated deadline, Anie needs 5 hours extra aside from the normal work schedule each day. If each day her work schedule requires her to be productive for 10 hours, and the project is estimated to take 1500 hours, calculate the number of days it would take Anie to finish the job."""
    # Define the number of productive hours per day
    productive_hours_per_day = 10

    # Calculate the total number of hours Anie can work in a day
    total_working_hours_per_day = productive_hours_per_day + 5

    # Define the total number of hours required to complete the project
    total_project_hours = 1500

    # Calculate the number of days required to complete the project
    project_days = total_project_hours / total_working_hours_per_day

    # Round up the number of days to the nearest whole number
    project_days = round(project_days)

    # return the result
    result = project_days
    return result

print(solution())