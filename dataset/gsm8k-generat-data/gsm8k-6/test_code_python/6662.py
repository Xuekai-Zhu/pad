def solution():
    # Calculate Queenie's total earnings for 5 days with 4 hours overtime
    regular_pay = 150 * 5  # Queenie earns $150 a day for 5 days
    overtime_pay = 5 * 4 * 5  # Queenie earns $5 per OT hour for 4 OT hours 
    total_earnings = regular_pay + overtime_pay
    result = total_earnings
    return result

print(solution())