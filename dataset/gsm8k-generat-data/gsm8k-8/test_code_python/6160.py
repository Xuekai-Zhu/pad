def solution():
    # Calculate Samantha's total payment if she pays in installments
    total_payment = 3000 + (30 * 300)

    # Calculate the amount of interest she would pay if she paid in installments
    installment_interest = total_payment - 8000

    # Calculate the amount she would save by paying cash
    savings = installment_interest
    result = savings
    return result

print(solution())