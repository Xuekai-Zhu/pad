def solution():
    # Starting amount in Emma's bank account
    starting_amount = 230

    # Amount Emma withdrew
    withdraw_amount = 60

    # Amount Emma deposited the week after
    deposit_amount = 2 * withdraw_amount

    # Calculate the new balance in Emma's bank account
    new_balance = starting_amount - withdraw_amount + deposit_amount

    result = new_balance
    return result

print(solution())