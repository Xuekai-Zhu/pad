def solution():
    initial_amount = 100
    weekly_spending = 8
    num_days = 7
    withdrawal_amount = 5

    # Calculate the total amount spent during the week
    total_spending = weekly_spending * num_days

    # Calculate the amount remaining in the account after spending
    remaining_amount = initial_amount - total_spending

    # Calculate the number of $5 bills that can be withdrawn
    num_bills = remaining_amount // withdrawal_amount

    # Calculate the total amount withdrawn in $5 bills
    withdrawal_total = num_bills * withdrawal_amount

    # Calculate the remaining amount after withdrawal
    remaining_after_withdrawal = remaining_amount - withdrawal_total
    result = remaining_after_withdrawal
    return result

print(solution())