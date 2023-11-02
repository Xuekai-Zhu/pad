def solution():
    
    monthly_pay = 1000
    raise_percent = 10
    total_pay = (monthly_pay * 2) + (monthly_pay * (raise_percent / 100))
    result = total_pay
    return result

print(solution())