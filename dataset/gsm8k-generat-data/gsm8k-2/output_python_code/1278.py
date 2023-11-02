def solution():
    """Bill is buying healthcare on an exchange. The normal monthly price of the plan he wants is $500. The government will pay for part of this cost depending on Bill's income: 90% if he makes less than $10,000, 50% if he makes between $10,001 and $40,000, and 20% if he makes more than $50,000. Bill earns $25/hour and works 30 hours per week, four weeks per month. How much will Bill spend for health insurance in a year?"""
    hourly_rate = 25
    weekly_pay = hourly_rate * 30
    monthly_pay = weekly_pay * 4
    total_annual_income = monthly_pay * 12
    monthly_plan_cost = 500
    if total_annual_income < 10000:
        gov_pay = monthly_plan_cost * 0.9
    elif total_annual_income >= 10001 and total_annual_income <= 40000:
        gov_pay = monthly_plan_cost * 0.5
    else:
        gov_pay = monthly_plan_cost * 0.2
    out_of_pocket = monthly_plan_cost - gov_pay
    annual_out_of_pocket = out_of_pocket * 12
    result = annual_out_of_pocket
    return result

print(solution())