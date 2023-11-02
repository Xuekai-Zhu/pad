def solution():
    starting_amount = 230  # Emma starts with $230 in her bank account
    withdrawal_amount = 60  # Emma withdraws $60 to buy shoes

    # Calculate the amount Emma deposits next week
    deposit_amount = withdrawal_amount * 2

    # Calculate the total amount left in Emma's bank account
    total_amount = starting_amount - withdrawal_amount + deposit_amount

    result = total_amount
    return result

print(solution())