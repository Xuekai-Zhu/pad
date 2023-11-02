def solution():
    
    machine_cost = 120
    down_payment = machine_cost / 2
    balance = machine_cost - down_payment
    days_to_pay = 10
    daily_minimum_payment = balance / days_to_pay
    result = daily_minimum_payment
    return result

print(solution())