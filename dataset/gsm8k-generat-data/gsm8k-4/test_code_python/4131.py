def solution():
    """Bill's take-home salary is $40,000. He pays $2,000 in property taxes, $3,000 in sales taxes, and 10% of his gross salary in income taxes. What is Bill's gross salary?"""
    # Define the variables
    take_home_salary = 40000
    property_taxes = 2000
    sales_taxes = 3000
    income_tax_rate = 0.1

    # Calculate the income tax
    income_tax = (take_home_salary + property_taxes + sales_taxes) / (1 - income_tax_rate) - take_home_salary - property_taxes - sales_taxes

    # Calculate the gross salary
    gross_salary = take_home_salary + property_taxes + sales_taxes + income_tax

    # Return the result
    result = gross_salary
    return result

print(solution())