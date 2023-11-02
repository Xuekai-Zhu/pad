def solution():
    days_per_week = 5
    paid_vacation_days = 6
    unpaid_vacation_days = days_per_week - paid_vacation_days
    hourly_wage = 15
    hours_per_day = 8
    total_hours_unpaid = unpaid_vacation_days * hours_per_day
    total_pay_unpaid = total_hours_unpaid * hourly_wage
    result = total_pay_unpaid
    return result

print(solution())