def solution():
    """Walter works 5 days a week in a fast-food chain and earns $5 per hour. Since he is a working student, he can only work 4 hours a day and allocates 3/4 of his weekly earning for his schooling. How much does he allocate for school?"""
    # Define Walter's work schedule
    DAYS_WORKED = 5
    HOURS_PER_DAY = 4
    HOURLY_WAGE = 5

    # Calculate Walter's weekly earnings
    weekly_earnings = DAYS_WORKED * HOURS_PER_DAY * HOURLY_WAGE

    # Calculate the amount of money Walter allocates for school
    school_allocation = weekly_earnings * 3 / 4

    # Display the amount of money Walter allocates for school
    result = school_allocation
    return result

print(solution())