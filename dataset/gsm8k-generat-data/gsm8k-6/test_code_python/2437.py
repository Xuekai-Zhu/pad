def solution():
    starting_balance = 100  # initial balance in Emma's account
    daily_expenses = 8  # amount Emma spends each day
    remaining_balance = starting_balance - (daily_expenses * 7)  # balance remaining at the end of the week
    num_5_bills = remaining_balance // 5  # number of $5 bills Emma can get from the bank
    remaining_balance -= (num_5_bills * 5)  # subtract the amount given in $5 bills from remaining balance
    result = remaining_balance
    return result

print(solution())