def solution():
    check_amount = 15.00
    tax_rate = 0.20
    tax_amount = check_amount * tax_rate
    total_amount = check_amount + tax_amount
    tip_amount = 20.00 - total_amount
    result = tip_amount
    return result

print(solution())