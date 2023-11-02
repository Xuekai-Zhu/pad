def solution():
    """Javier exercised for 50 minutes every day for one week. Sanda exercised for 90 minutes on each of three days. How many minutes did Javier and Sanda exercise in total?"""
    # Define the number of days in a week
    DAYS_IN_WEEK = 7

    # Define the exercise times for Javier and Sanda
    javier_time = 50 * DAYS_IN_WEEK
    sanda_time = 90 * 3

    # Calculate the total exercise time
    total_time = javier_time + sanda_time

    # return the result
    result = total_time
    return result

print(solution())