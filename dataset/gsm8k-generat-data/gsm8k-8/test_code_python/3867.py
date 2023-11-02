def solution():
    total_workdays = 10
    paid_vacation_days = 6
    unpaid_vacation_days = total_workdays - paid_vacation_days

    daily_pay = 15 * 8

    unpaid_vacation_pay_loss = daily_pay * unpaid_vacation_days

    result = unpaid_vacation_pay_loss
    return result

print(solution())