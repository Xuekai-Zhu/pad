def solution():
    """Janet is trying to decide whether to quit her job and start freelancing. She works 40 hours a week at both jobs. She gets paid $30/hour at her current job, and would get paid $40/hour as a freelancer. However, she'd have to pay an extra $25 a week in FICA taxes plus $400/month in healthcare premiums. How much more would Janet make per month as a freelancer if there are four weeks in a month?"""
    hours_per_week = 40
    hourly_rate_current_job = 30
    hourly_rate_freelancer = 40
    extra_FICA_taxes = 25 * 4
    healthcare_premiums = 400
    monthly_income_current_job = hours_per_week * hourly_rate_current_job * 4
    monthly_income_freelancer = hours_per_week * hourly_rate_freelancer * 4 - extra_FICA_taxes - healthcare_premiums
    extra_monthly_income = monthly_income_freelancer - monthly_income_current_job
    result = extra_monthly_income
    return result

print(solution())