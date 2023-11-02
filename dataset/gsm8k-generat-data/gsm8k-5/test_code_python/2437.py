def solution():
    balance = 100  # Emma starts with $100 in her account
    daily_spending = 8  # Emma spends $8 every day
    days_in_week = 7  # There are 7 days in a week

    # Calculate Emma's balance after one week of spending
    balance -= daily_spending * days_in_week

    # Calculate the maximum number of $5 bills Emma can get from her remaining balance
    num_bills = balance // 5

    # Calculate Emma's remaining balance after getting $5 bills
    remaining_balance = balance - num_bills * 5
    result = remaining_balance
    return result

print(solution())