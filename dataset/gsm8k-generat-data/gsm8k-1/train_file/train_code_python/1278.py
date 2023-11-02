def solution():
    """Bill is buying healthcare on an exchange. The normal monthly price of the plan he wants is $500. The government will pay for part of this cost depending on Bill's income: 90% if he makes less than $10,000, 50% if he makes between $10,001 and $40,000, and 20% if he makes more than $50,000. Bill earns $25/hour and works 30 hours per week, four weeks per month. How much will Bill spend for health insurance in a year?"""
    monthly_healthcare_cost = 500
    annual_income = 25 * 30 * 4 * 12 # $36,000 per year
    if annual_income < 10000:
        government_contribution = monthly_healthcare_cost * 0.9
    elif annual_income < 40000:
        government_contribution = monthly_healthcare_cost * 0.5
    elif annual_income > 50000:
        government_contribution = monthly_healthcare_cost * 0.2
    else:
        government_contribution = 0
    bill_amount = monthly_healthcare_cost - government_contribution
    total_cost = bill_amount * 12
    result = total_cost
    return result

print(solution())