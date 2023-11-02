def solution():
    """Vikki worked 42 hours in one week. Her hourly pay rate is $10. From her weekly earnings, 20% is deducted as tax, 5% is deducted as insurance cover, and $5 is deducted for union dues. How much money, in dollars, does Vikki take home after deductions?"""
    # Define Vikki's hourly pay rate and the number of hours worked
    pay_rate = 10
    hours_worked = 42

    # Calculate Vikki's gross pay (before deductions)
    gross_pay = pay_rate * hours_worked

    # Calculate the amount of tax, insurance, and union dues deducted from Vikki's gross pay
    tax_deduction = gross_pay * 0.2
    insurance_deduction = gross_pay * 0.05
    union_dues = 5
    total_deductions = tax_deduction + insurance_deduction + union_dues

    # Calculate Vikki's net pay (after deductions)
    net_pay = gross_pay - total_deductions

    # Return the result
    result = net_pay
    return result

print(solution())