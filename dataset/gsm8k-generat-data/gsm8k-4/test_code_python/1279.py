def solution():
    """Bill is buying healthcare on an exchange. The normal monthly price of the plan he wants is $500. The government will pay for part of this cost depending on Bill's income: 90% if he makes less than $10,000, 50% if he makes between $10,001 and $40,000, and 20% if he makes more than $50,000. Bill earns $25/hour and works 30 hours per week, four weeks per month. How much will Bill spend for health insurance in a year?"""
    # Calculate Bill's annual income
    hourly_rate = 25
    hours_per_week = 30
    weeks_per_month = 4
    monthly_income = hourly_rate * hours_per_week * weeks_per_month
    annual_income = monthly_income * 12

    # Determine the percentage of the cost that will be covered by the government based on Bill's income
    if annual_income < 10000:
        government_coverage = 0.9
    elif annual_income <= 40000:
        government_coverage = 0.5
    else:
        government_coverage = 0.2

    # Calculate the monthly cost of the insurance for Bill
    normal_monthly_price = 500
    monthly_cost = normal_monthly_price * (1 - government_coverage)

    # Calculate the annual cost of the insurance for Bill
    annual_cost = monthly_cost * 12

    result = annual_cost
    return result

print(solution())