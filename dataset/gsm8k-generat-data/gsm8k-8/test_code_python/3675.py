def solution():
    # Define the initial loan amount and finance fee
    loan_amount = 100
    finance_fee = 0.05

    # Calculate the total finance fee for each week
    total_fee = finance_fee
    for i in range(1, 2):
        finance_fee *= 2
        total_fee += finance_fee

    # Calculate the total fees for the two weeks
    total_fees = total_fee * loan_amount

    result = total_fees
    return result

print(solution())