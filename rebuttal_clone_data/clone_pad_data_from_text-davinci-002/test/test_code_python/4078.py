def solution():
    coupe_price = 30000
    SUV_price = 2 * coupe_price
    commission_percentage = 2
    commission_coupe = coupe_price * (commission_percentage / 100)
    commission_SUV = SUV_price * (commission_percentage / 100)
    total_commission = commission_coupe + commission_SUV
    result = total_commission
    return result

print(solution())