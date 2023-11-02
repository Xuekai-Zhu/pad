def solution():
    salary = 5000
    tax_rate = 0.1
    after_tax_salary = salary * (1 - tax_rate)
    late_payment_cost = after_tax_salary * (3/5)

    # Calculate the monthly rent expense
    rent_expense = late_payment_cost / 2
    result = rent_expense
    return result

print(solution())