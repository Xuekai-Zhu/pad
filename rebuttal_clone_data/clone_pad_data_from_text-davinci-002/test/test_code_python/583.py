def solution():
    sale_one = 157000
    sale_two = 499000
    sale_three = 125000
    commission_rate = 0.02
    commission_one = sale_one * commission_rate
    commission_two = sale_two * commission_rate
    commission_three = sale_three * commission_rate
    total_commission = commission_one + commission_two + commission_three
    result = total_commission
    
    return result

print(solution())