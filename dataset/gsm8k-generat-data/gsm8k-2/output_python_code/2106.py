def solution():
    """Rhett has been late on two of his monthly rent payments, but his landlord does not charge late fees and so he will be able to pay their total cost with 3/5 of his next month's salary after taxes. If he is currently paid $5000 per month and has to pay 10% tax, calculate his rent expense per month?"""
    monthly_salary = 5000
    tax_rate = 0.1
    after_tax_salary = monthly_salary * (1 - tax_rate)
    late_payments_total = 2 * 1000  # assuming rent is $1000/month
    available_for_rent = after_tax_salary * (3 / 5)
    rent_per_month = (late_payments_total + available_for_rent) / 3
    result = round(rent_per_month, 2)
    return result

print(solution())