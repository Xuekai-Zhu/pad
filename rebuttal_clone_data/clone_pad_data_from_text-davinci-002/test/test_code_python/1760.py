def solution():
    hours_worked = 3
    hourly_rate = 15
    total_pay = hours_worked * hourly_rate
    tip_percent = 20
    tip_amount = total_pay * (tip_percent / 100)
    total_amount_paid = total_pay + tip_amount
    result = total_amount_paid
    
    return result

print(solution())