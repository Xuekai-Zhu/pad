def solution():
    
    investment_A = 300
    investment_B = 200
    interest_rate_A = 30
    interest_rate_B = 50
    
    
    amount_A = investment_A + (investment_A * (interest_rate_A / 100))
    amount_B = investment_B + (investment_B * (interest_rate_B / 100))
    
    
    difference = amount_A - amount_B
    result = difference
    return result

print(solution())