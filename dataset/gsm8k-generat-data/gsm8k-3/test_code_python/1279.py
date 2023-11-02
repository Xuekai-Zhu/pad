def solution():
    """Bill is buying healthcare on an exchange. The normal monthly price of the plan he wants is $500. The government will pay for part of this cost depending on Bill's income: 90% if he makes less than $10,000, 50% if he makes between $10,001 and $40,000, and 20% if he makes more than $50,000. Bill earns $25/hour and works 30 hours per week, four weeks per month. How much will Bill spend for health insurance in a year?"""
    # Define the cost of the health insurance plan
    PLAN_COST = 500

    # Define Bill's income
    hourly_wage = 25
    hours_per_week = 30
    weeks_per_month = 4
    annual_income = hourly_wage * hours_per_week * weeks_per_month * 12

    # Calculate the government subsidy percentage based on Bill's income
    if annual_income < 10000:
        subsidy_percentage = 0.9
    elif 10001 <= annual_income <= 40000:
        subsidy_percentage = 0.5
    elif annual_income > 50000:
        subsidy_percentage = 0.2
    else:
        subsidy_percentage = 0

    # Calculate the monthly cost of the plan after the government subsidy
    subsidized_cost = PLAN_COST * (1 - subsidy_percentage)

    # Calculate the annual cost of the plan after the government subsidy
    annual_cost = subsidized_cost * 12

    # Display the annual cost of the plan after the government subsidy
    result = annual_cost
    return result

print(solution())