def solution():
    """Bill's take-home salary is $40,000. He pays $2,000 in property taxes, $3,000 in sales taxes, and 10% of his gross salary in income taxes. What is Bill's gross salary?"""
    # Define the amounts paid in taxes
    PROPERTY_TAX = 2000
    SALES_TAX = 3000
    INCOME_TAX_RATE = 0.1

    # Define the take-home salary
    take_home_salary = 40000

    # Calculate Bill's gross salary
    gross_salary = (take_home_salary + PROPERTY_TAX + SALES_TAX) / (1 - INCOME_TAX_RATE)

    # Display Bill's gross salary
    result = gross_salary
    return result

print(solution())