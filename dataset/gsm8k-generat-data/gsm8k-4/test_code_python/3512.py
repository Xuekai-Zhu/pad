def solution():
    """Roy spends 2 hours on sports activities in school every day. He goes to school 5 days a week. If he missed 2 days within a week, how many hours did he spend on sports in school that week?"""
    # Define the number of days Roy goes to school in a week
    days_in_week = 5

    # Define the number of hours Roy spends on sports activities per day
    hours_per_day = 2

    # Define the number of days Roy missed
    days_missed = 2

    # Calculate the total number of hours Roy spends on sports activities in school in a week
    total_hours = (days_in_week - days_missed) * hours_per_day

    # return the result
    result = total_hours
    return result

print(solution())