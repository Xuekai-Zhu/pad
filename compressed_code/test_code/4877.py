def solution():
    
    total_cost = 13380
    down_payment = 5400
    monthly_payment = 420
    remaining_balance = total_cost - down_payment
    months_to_pay = remaining_balance / monthly_payment
    result = months_to_pay
    return result

print(solution())