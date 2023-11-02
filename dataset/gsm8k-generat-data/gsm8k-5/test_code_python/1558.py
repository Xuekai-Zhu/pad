def solution():
    hours_per_week = 40  # Janet works 40 hours per week
    hourly_pay_current_job = 30  # Janet makes $30 per hour at her current job
    hourly_pay_freelancing = 40  # Janet would make $40 per hour freelancing
    fica_taxes = 25  # Janet pays an extra $25 per week in FICA taxes as a freelancer
    healthcare_premiums = 400  # Janet pays $400 per month in healthcare premiums as a freelancer

    # Calculate the total monthly income from Janet's current job
    monthly_income_current_job = hours_per_week * hourly_pay_current_job * 4

    # Calculate the total monthly income from freelancing
    monthly_income_freelancing = (hours_per_week * hourly_pay_freelancing * 4) - (fica_taxes * 4) - healthcare_premiums

    # Calculate the difference in monthly income between the two jobs
    difference_monthly_income = monthly_income_freelancing - monthly_income_current_job
    result = difference_monthly_income
    return result

print(solution())