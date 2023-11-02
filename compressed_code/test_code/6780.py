def solution():
    
    total_cost = 280000
    deposit = 40000
    balance = total_cost - deposit
    years = 10
    months = years * 12
    monthly_payment = balance / months / 1000
    result = monthly_payment
    return result

print(solution())