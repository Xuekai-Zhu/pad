def solution():
    hours_per_week = 40
    current_pay_rate = 30
    freelancer_pay_rate = 40
    extra_fica_taxes = 25
    healthcare_premiums = 400
    weeks_per_month = 4

    # Calculate the total monthly income at the current job
    current_monthly_income = hours_per_week * current_pay_rate * weeks_per_month

    # Calculate the total monthly income as a freelancer
    freelancer_monthly_income = hours_per_week * freelancer_pay_rate * weeks_per_month

    # Calculate the total monthly expenses as a freelancer
    freelancer_expenses = extra_fica_taxes * weeks_per_month + healthcare_premiums

    # Calculate the difference between the monthly income as a freelancer and the monthly expenses
    difference = freelancer_monthly_income - freelancer_expenses - current_monthly_income

    result = difference
    return result

print(solution())