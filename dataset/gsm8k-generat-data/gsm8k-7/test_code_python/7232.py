def solution():
    starting_balance = 230
    withdrawal_amount = 60
    deposit_amount = withdrawal_amount * 2

    remaining_balance = starting_balance - withdrawal_amount + deposit_amount
    result = remaining_balance
    return result

print(solution())