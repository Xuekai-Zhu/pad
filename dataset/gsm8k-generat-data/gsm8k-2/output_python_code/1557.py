def solution():
    """Janet is trying to decide whether to quit her job and start freelancing. She works 40 hours a week at both jobs. She get paid $30/hour at her current job, and would get paid $40/hour as a freelancer. However, she'd have to pay an extra $25 a week in FICA taxes plus $400/month in healthcare premiums. How much more would Janet make per month as a freelancer if there are four weeks in a month?"""
    current_pay = 30 * 40 * 4
    freelance_pay = 40 * 40 * 4
    fica_taxes = 25 * 4
    healthcare_premiums = 400
    total_freelance_expenses = fica_taxes + healthcare_premiums
    total_freelance_pay = freelance_pay - total_freelance_expenses
    monthly_pay_increase = total_freelance_pay - current_pay
    result = monthly_pay_increase
    return result

print(solution())