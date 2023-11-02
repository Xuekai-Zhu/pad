def solution():
    
    wife_savings = 100 * 4 * 4  
    husband_savings = 225 * 4  
    total_savings = wife_savings + husband_savings
    investment_amount = total_savings / 2
    shares = investment_amount / 50
    result = shares
    return result

print(solution())