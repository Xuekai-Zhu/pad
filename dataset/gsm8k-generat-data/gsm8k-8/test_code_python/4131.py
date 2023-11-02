def solution():
    # Define the values given in the problem
    take_home_salary = 40000
    property_taxes = 2000
    sales_taxes = 3000
    income_tax_rate = 0.1

    # Calculate income tax
    income_tax = (take_home_salary + property_taxes + sales_taxes) / (1 - income_tax_rate) - take_home_salary - property_taxes - sales_taxes

    # Calculate gross salary
    gross_salary = take_home_salary + property_taxes + sales_taxes + income_tax

    result = gross_salary
    return result

print(solution())