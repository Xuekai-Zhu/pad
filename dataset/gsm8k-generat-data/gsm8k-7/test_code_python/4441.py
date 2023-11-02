def solution():
    starting_balance = 150
    last_month_deposit = 17
    this_month_deposit = 21
    this_month_balance = starting_balance + last_month_deposit - withdrawal + this_month_deposit + 16

    # Calculate the amount of money withdrawn last month
    withdrawal = this_month_balance - starting_balance - last_month_deposit - this_month_deposit + 16
    result = withdrawal
    return result

print(solution())