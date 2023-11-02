def solution():
    # Calculate the total amount paid in installment
    installment_total = 100 + (40*4) + (35*4) + (30*4)

    # Calculate the amount saved by buying the tablet in cash
    cash_total = 450
    savings = installment_total - cash_total
    result = savings
    return result

print(solution())