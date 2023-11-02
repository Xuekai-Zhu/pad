def solution():
    # Calculate the total amount paid on the installment plan
    installment_total = 100 + (40*4) + (35*4) + (30*4)

    # Calculate the difference between the total paid on installment and the cash price
    savings = 450 - installment_total
    result = savings
    return result

print(solution())