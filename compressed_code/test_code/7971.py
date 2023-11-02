def solution():
    
    kyro_debt = 1200 / 2
    aryan_debt = 1200
    kyro_paid = kyro_debt * 0.8
    aryan_paid = aryan_debt * 0.6
    total_paid = kyro_paid + aryan_paid
    total_savings = 300 + total_paid
    result = total_savings
    return result

print(solution())