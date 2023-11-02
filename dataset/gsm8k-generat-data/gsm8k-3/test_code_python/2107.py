def solution():
    """Rhett has been late on two of his monthly rent payments, but his landlord does not charge late fees and so he will be able to pay their total cost with 3/5 of his next month's salary after taxes. If he is currently paid $5000 per month and has to pay 10% tax, calculate his rent expense per month?"""
    # Calculate Rhett's monthly income after taxes
    tax = 0.1
    monthly_income_after_tax = 5000 * (1 - tax)

    # Calculate the total cost of the two late rent payments
    late_rent_total = 2000

    # Calculate the amount Rhett will be able to pay towards the late rent payments
    amount_to_pay = monthly_income_after_tax * 3/5

    # Calculate Rhett's monthly rent expense
    rent_expense = (late_rent_total - amount_to_pay)/2

    # Display the monthly rent expense
    result = rent_expense
    return result

print(solution())