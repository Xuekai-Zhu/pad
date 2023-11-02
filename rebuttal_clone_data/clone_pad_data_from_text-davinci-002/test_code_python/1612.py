def solution():
    hourly_wage = 12.5
    taxes_and_fees = 20
    hours_worked = 40
    paycheck = hourly_wage * hours_worked
    taxes = paycheck * (taxes_and_fees / 100)
    gummy_bears = 15
    after_gummy_bears = paycheck * (gummy_bears / 100)
    result = paycheck - taxes - after_gummy_bears
    return result

print(solution())