def solution():
    
    total_cost = 18000
    initial_payment = 3000
    remaining_cost = total_cost - initial_payment
    months_to_pay = 6
    monthly_payment = remaining_cost / months_to_pay
    result = monthly_payment
    return result

print(solution())