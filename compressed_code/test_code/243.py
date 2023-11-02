def solution():
    
    annual_earnings = 60000
    tax_rate = 0.18
    tax_amount = annual_earnings * tax_rate
    net_earnings = annual_earnings - tax_amount
    result = net_earnings
    return result

print(solution())