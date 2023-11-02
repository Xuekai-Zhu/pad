def solution():
    
    # Define the cost per session and the number of students rented per week
    SESSION_COST = 25
    REnt_PER_WEEK = 1.5

    # Define the number of students per session and the number of days per week
    STUDENTS_PER_WEEK = 10
    DAYS_PER_WEEK = 3

    # Calculate the total number of sessions in a month
    sessions_per_month = STUDENTS_PER_WEEK * DAYS_PER_WEEK * 4

    # Calculate the expected earnings per month
    expected_earnings_per_month = sessions_per_month * REENT_COST

    # Display the expected earnings per month
    result = expected_earnings_per_month
    return result

print(solution())