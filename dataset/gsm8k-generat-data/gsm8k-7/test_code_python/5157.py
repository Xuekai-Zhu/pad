def solution():
    check_amount = 15.0
    tax_rate = 0.2
    bill_amount = 20.0

    # Calculate the tax amount
    tax_amount = check_amount * tax_rate

    # Calculate the total amount with tax
    total_amount = check_amount + tax_amount

    # Calculate the tip amount
    tip_amount = bill_amount - total_amount
    result = tip_amount
    return result

print(solution())