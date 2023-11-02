def solution():
    take_home_salary = 40000  # Bill's take-home salary is $40,000
    property_taxes = 2000  # Bill pays $2,000 in property taxes
    sales_taxes = 3000  # Bill pays $3,000 in sales taxes
    income_tax_rate = 0.1  # Bill pays 10% of his gross salary in income taxes

    # Calculate the total amount of taxes Bill pays
    total_taxes = property_taxes + sales_taxes + (income_tax_rate * gross_salary)

    # Calculate Bill's gross salary using the formula: Gross salary = Take-home salary + Total taxes
    gross_salary = take_home_salary + total_taxes
    result = gross_salary
    return result

print(solution())