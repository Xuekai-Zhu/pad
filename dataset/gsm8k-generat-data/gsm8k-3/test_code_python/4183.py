def solution():
    """A country used to have a tax rate of 20%.  They raised it to 30%.  In that same time frame, John went from making 1,000,000 a year to 1,500,000 a year.  How much more does he pay in taxes now compared to then?"""
    # Define the old and new tax rates
    OLD_TAX_RATE = 0.2
    NEW_TAX_RATE = 0.3

    # Define John's old and new annual income
    OLD_INCOME = 1000000
    NEW_INCOME = 1500000

    # Calculate John's old and new taxes
    old_taxes = OLD_INCOME * OLD_TAX_RATE
    new_taxes = NEW_INCOME * NEW_TAX_RATE

    # Calculate the difference in John's taxes
    difference = new_taxes - old_taxes

    # Display the difference in John's taxes
    result = difference
    return result

print(solution())