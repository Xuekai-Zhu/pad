def solution():
    
    down_payment = 108000
    savings_time = 3  
    total_savings = down_payment / savings_time
    monthly_savings = total_savings / 12
    amount_per_person = monthly_savings / 2
    result = amount_per_person
    return result

print(solution())