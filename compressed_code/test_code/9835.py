def solution():
    
    check_amount = 15
    tax_percent = 20
    tax_amount = check_amount * (tax_percent / 100)
    total_amount = check_amount + tax_amount
    tip_amount = 20 - total_amount
    result = tip_amount
    return result

print(solution())