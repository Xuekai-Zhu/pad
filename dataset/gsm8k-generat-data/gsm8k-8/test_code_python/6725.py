def solution():
    # Define the variables
    days_worked = 5
    regular_pay = 30
    overtime_pay = regular_pay + 15
    overtime_shifts = 3

    # Calculate total earnings without overtime
    regular_earnings = days_worked * regular_pay

    # Calculate total earnings with overtime
    overtime_earnings = overtime_shifts * 2 * overtime_pay

    # Calculate total earnings for the week
    total_earnings = regular_earnings + overtime_earnings
    result = total_earnings
    return result

print(solution())