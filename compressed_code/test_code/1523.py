def solution():
    
    sales = 24000
    commission_rate = 0.12
    commission_earned = sales * commission_rate
    personal_needs = 0.6 * commission_earned
    savings = commission_earned - personal_needs
    result = savings
    return result

print(solution())