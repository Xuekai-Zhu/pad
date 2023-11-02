def solution():
    """Rhett has been late on two of his monthly rent payments, but his landlord does not charge late fees and so he will be able to pay their total cost with 3/5 of his next month's salary after taxes. If he is currently paid $5000 per month and has to pay 10% tax, calculate his rent expense per month?"""
    # Define Rhett's monthly salary and tax rate
    salary = 5000
    tax_rate = 0.1

    # Calculate Rhett's monthly after-tax income
    after_tax_income = salary - (salary * tax_rate)

    # Calculate the total cost of Rhett's late rent payments
    late_rent_cost = 2 * 1000

    # Calculate the amount Rhett will have available to pay rent next month
    available_rent_funds = (3/5) * after_tax_income

    # Calculate Rhett's monthly rent expense
    rent_expense = (late_rent_cost + available_rent_funds) / 3

    # return the result
    result = rent_expense
    return result

print(solution())