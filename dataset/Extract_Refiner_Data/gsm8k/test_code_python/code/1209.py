def solution():
    
    borrowed_amount = 300
    interest_rate = 0.02
    total_interest = borrowed_amount * interest_rate
    total_amount = borrowed_amount + total_interest
    monthly_payment = 25
    months_worked = 11
    twelfth_month_payment = total_amount - (total_interest * months_worked)
    result = twelfth_month_payment
    return result

print(solution())