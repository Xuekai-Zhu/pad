def solution():
    debt_amount = 100
    initial_payment = 40
    hourly_rate = 15
    remaining_debt = debt_amount - initial_payment
    hours_worked = remaining_debt / hourly_rate
    result = hours_worked
    return result

print(solution())