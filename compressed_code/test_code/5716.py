def solution():
    
    hourly_pay = 50
    hours_worked = 10
    total_earned = hourly_pay * hours_worked
    withholding_percent = 0.2
    withheld_amount = total_earned * withholding_percent
    amount_received = total_earned - withheld_amount
    result = amount_received
    return result

print(solution())