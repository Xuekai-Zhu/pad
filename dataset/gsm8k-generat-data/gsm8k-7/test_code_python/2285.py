def solution():
    mom_transfer = 60
    sis_transfer = mom_transfer / 2
    remaining_balance = 100

    # Calculate the total amount transferred out of the account
    total_transfer = mom_transfer + sis_transfer

    # Calculate the starting balance in the account
    starting_balance = remaining_balance + total_transfer
    result = starting_balance
    return result

print(solution())