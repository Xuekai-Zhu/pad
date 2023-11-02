def solution():
    """George donated half his monthly income to charity and spent $20 from the other half on groceries. If he now has $100 left, how much was his monthly income?"""
    # Define the variables
    income = 0
    donation = 0
    groceries = 20

    # Set up an equation based on the given information
    # Half of the income was donated
    # The other half minus $20 was what was left
    # Therefore, the equation is: donation + (income / 2 - 20) + 100 = income / 2

    # Simplifying the equation gives us:
    # donation = income / 4 - 60

    # We also know that donation = income / 2, so we can say:
    # income / 2 = income / 4 - 60

    # Solving for income gives us:
    income = 240

    # Display the monthly income
    result = income
    return result

print(solution())