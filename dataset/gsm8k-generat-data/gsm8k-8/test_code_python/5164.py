def solution():
    # Define the amount of money Tye withdraws from each bank
    withdraw_amount = 300

    # Calculate the number of $20 bills Tye receives from each bank
    bills_per_bank = withdraw_amount / 20

    # Calculate the total number of $20 bills Tye receives
    total_bills = bills_per_bank * 2

    result = total_bills
    return result

print(solution())