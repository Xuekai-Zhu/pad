def solution():
    balance = 150
    finance_charge = 0.02

    # Calculate the amount of finance charge
    total_finance_charge = balance * finance_charge

    # Calculate the total amount to be paid by Mr. Smith
    total_amount = balance + total_finance_charge
    result = total_amount
    return result

print(solution())