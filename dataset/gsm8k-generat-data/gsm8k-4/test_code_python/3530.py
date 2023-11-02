def solution():
    """Walter works 5 days a week in a fast-food chain and earns $5 per hour. Since he is a working student, he can only work 4 hours a day and allocates 3/4 of his weekly earning for his schooling. How much does he allocate for school?"""
    # Define the number of days worked and the hourly rate
    days_worked = 5
    hourly_rate = 5

    # Define the number of hours worked each day
    hours_per_day = 4

    # Calculate the total number of hours worked in a week
    total_hours = days_worked * hours_per_day

    # Calculate the total earning for the week
    total_earning = total_hours * hourly_rate

    # Calculate the amount allocated for schooling
    school_allocation = total_earning * (3/4)

    # Return the result
    result = school_allocation
    return result

print(solution())