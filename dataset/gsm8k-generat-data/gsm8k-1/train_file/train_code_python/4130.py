def solution():
    """Bill's take-home salary is $40,000. He pays $2,000 in property taxes, $3,000 in sales taxes, and 10% of his gross salary in income taxes. What is Bill's gross salary?"""
    take_home_salary = 40000
    property_taxes = 2000
    sales_taxes = 3000
    income_tax_rate = 0.1
    total_taxes = property_taxes + sales_taxes + (income_tax_rate * gross_salary)
    gross_salary = (take_home_salary + total_taxes) / (1 - income_tax_rate)
    result = gross_salary
    return result

print(solution())