def solution():
    """Hannah is trying to figure out how much she'll get paid this week. She makes $30/hour and works 18 hours per week. Her pay is docked $5 each time she's late. If she was late 3 times this week, how much does she get paid?"""
    # Define Hannah's hourly rate and number of hours worked
    hourly_rate = 30
    hours_worked = 18

    # Define the amount docked for each time Hannah is late
    late_dock = 5

    # Calculate Hannah's base pay before any deductions
    base_pay = hourly_rate * hours_worked

    # Calculate the total amount docked for being late
    late_deduction = late_dock * 3

    # Calculate Hannah's final pay after all deductions
    final_pay = base_pay - late_deduction

    result = final_pay
    return result

print(solution())