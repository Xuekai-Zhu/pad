def solution():
    """Vikki worked 42 hours in one week. Her hourly pay rate is $10. From her weekly earnings, 20% is deducted as tax, 5% is deducted as insurance cover, and $5 is deducted for union dues. How much money, in dollars, does Vikki take home after deductions?"""
    # Define Vikki's hourly pay rate
    HOURLY_RATE = 10

    # Calculate Vikki's earnings before deductions
    earnings = HOURLY_RATE * 42

    # Calculate the total deductions
    tax_deduction = 0.2 * earnings
    insurance_deduction = 0.05 * earnings
    union_dues = 5
    total_deductions = tax_deduction + insurance_deduction + union_dues

    # Calculate Vikki's take-home pay
    take_home_pay = earnings - total_deductions

    # Display Vikki's take-home pay
    result = take_home_pay
    return result

print(solution())