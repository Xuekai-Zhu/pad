def solution():
    
    # Define the cost per session and per student
    SESSION_COST = 25
    STUDENT_COST = 1.5

    # Define the number of students rented per week and per month
    STUDENTS_PER_WEEK = 10
    STUDENTS_PER_MONTH = STUDENTS_PER_WEEK * 3 * 4

    # Calculate the expected earnings per month
    expected_earnings_per_month = STUDENTS_PER_MONTH * SESSION_COST + STUDENTS_PER_MONTH * STUDENT_COST

    # Display the expected earnings per month
    result = expected_earnings_per_month
    return result

print(solution())