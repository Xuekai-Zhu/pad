def solution():
    """A country used to have a tax rate of 20%. They raised it to 30%. In that same time frame, John went from making 1,000,000 a year to 1,500,000 a year. How much more does he pay in taxes now compared to then?"""
    # Define John's income and the old and new tax rates
    income_old = 1000000
    income_new = 1500000
    tax_rate_old = 0.2
    tax_rate_new = 0.3

    # Calculate John's old and new tax payments
    tax_old = income_old * tax_rate_old
    tax_new = income_new * tax_rate_new

    # Calculate the difference in tax payments
    tax_difference = tax_new - tax_old

    # Return the result
    result = tax_difference
    return result

print(solution())