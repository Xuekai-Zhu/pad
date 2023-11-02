def solution():
    # Calculate Bill's total tax payments
    total_taxes = 2000 + 3000 + 0.1 * gross_salary  # 10% of gross salary is paid in income taxes

    # Calculate Bill's gross salary
    # gross_salary - total_taxes = take-home salary
    # gross_salary = (take-home salary + total_taxes) / (1 - 0.1)  # 10% income tax rate
    gross_salary = (40000 + 2000 + 3000) / 0.9
    result = gross_salary
    return result

print(solution())