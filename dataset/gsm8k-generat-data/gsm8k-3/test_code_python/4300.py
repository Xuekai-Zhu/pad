def solution():
    """To finish the task assigned to her by the work supervisor in the stipulated deadline, Anie needs 5 hours extra aside from the normal work schedule each day.  If each day her work schedule requires her to be productive for 10 hours, and the project is estimated to take 1500 hours, calculate the number of days it would take Anie to finish the job."""
    # Define the normal work hours and extra hours
    NORMAL_HOURS = 10
    EXTRA_HOURS = 5

    # Define the total project hours
    PROJECT_HOURS = 1500

    # Calculate the total productive hours per day
    total_hours = NORMAL_HOURS + EXTRA_HOURS

    # Calculate the number of days needed to finish the project
    days_needed = PROJECT_HOURS / total_hours

    # Display the number of days needed
    result = days_needed
    return result

print(solution())