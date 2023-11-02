def solution():
    """Javier exercised for 50 minutes every day for one week. Sanda exercised for 90 minutes on each of three days. How many minutes did Javier and Sanda exercise in total?"""
    # Define the number of days and the length of each exercise session
    JAVIER_DAYS = 7
    JAVIER_MINUTES = 50
    SANDA_DAYS = 3
    SANDA_MINUTES = 90

    # Calculate the total time Javier exercised
    javier_total = JAVIER_DAYS * JAVIER_MINUTES

    # Calculate the total time Sanda exercised
    sanda_total = SANDA_DAYS * SANDA_MINUTES

    # Calculate the total time both exercised
    total_time = javier_total + sanda_total

    # Display the total time
    result = total_time
    return result

print(solution())