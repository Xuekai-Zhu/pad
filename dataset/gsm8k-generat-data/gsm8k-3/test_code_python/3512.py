def solution():
    """Roy spends 2 hours on sports activities in school every day. He goes to school 5 days a week. If he missed 2 days within a week, how many hours did he spend on sports in school that week?"""
    # Define the number of days Roy goes to school
    SCHOOL_DAYS = 5

    # Define the number of hours Roy spends on sports activities per day
    SPORTS_HOURS_PER_DAY = 2

    # Determine the number of days Roy missed
    missed_days = 2

    # Calculate the total number of hours Roy spent on sports activities in school that week
    total_hours = (SCHOOL_DAYS - missed_days) * SPORTS_HOURS_PER_DAY

    # Display the total number of hours
    result = total_hours
    return result

print(solution())