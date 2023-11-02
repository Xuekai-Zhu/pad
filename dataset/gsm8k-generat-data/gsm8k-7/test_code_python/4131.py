def solution():
    take_home_salary = 40000
    property_taxes = 2000
    sales_taxes = 3000
    income_tax_rate = 0.1

    # Calculate the total taxes paid
    total_taxes_paid = property_taxes + sales_taxes + (income_tax_rate * gross_salary)

    # Calculate the gross salary
    gross_salary = (take_home_salary + total_taxes_paid) / (1 - income_tax_rate)

    result = gross_salary
    return result

print(solution())