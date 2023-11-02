def solution():
    hourly_pay = 15
    hours_per_week = 40
    tax_rate = 20
    number_of_weeks = 52
    weekly_gross_pay = hourly_pay * hours_per_week
    weekly_net_pay = weekly_gross_pay * (1 - (tax_rate / 100))
    annual_net_pay = weekly_net_pay * number_of_weeks
    result = annual_net_pay
    return result

print(solution())