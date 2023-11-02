def solution():
    salary = 40000
    tax_rate = 0.2
    healthcare_rate = 0.1
    union_dues = 800

    # Calculate the amount of money Steve pays in taxes
    taxes = salary * tax_rate

    # Calculate the amount of money Steve pays for healthcare
    healthcare = salary * healthcare_rate

    # Calculate Steve's total deductions
    deductions = taxes + healthcare + union_dues

    # Calculate Steve's take-home pay
    take_home_pay = salary - deductions
    result = take_home_pay
    return result

print(solution())