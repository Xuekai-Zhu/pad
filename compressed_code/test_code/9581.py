def solution():
    
    monthly_cost = 12
    down_payment = 50
    time_period = 3 
    total_months = time_period * 12
    total_cost = (total_months * monthly_cost) + down_payment
    result = total_cost
    return result

print(solution())