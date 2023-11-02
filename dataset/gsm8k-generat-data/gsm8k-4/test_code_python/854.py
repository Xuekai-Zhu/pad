def solution():
    """Jeff committed to run for an hour a day during weekdays. On Thursday, he cut short his run by 20 minutes but was able to jog 10 minutes more on Friday. How many minutes was he able to run for that week?"""
    # Define the number of minutes Jeff committed to run each day
    DAILY_MINUTES = 60

    # Calculate the total number of minutes Jeff can run from Monday to Wednesday
    monday_to_wednesday = DAILY_MINUTES * 3

    # Calculate the number of minutes Jeff ran on Thursday
    thursday = DAILY_MINUTES - 20

    # Calculate the number of minutes Jeff ran on Friday
    friday = DAILY_MINUTES + 10

    # Calculate the total number of minutes Jeff ran for the week
    total_minutes = monday_to_wednesday + thursday + friday
    
    result = total_minutes
    return result

print(solution())