def solution():
    """Emma's bank account has $100 in it. Each day of the week, she spends $8. At the end of the week, she goes to the bank and asks for as many $5 bills as her account can give her. She leaves the rest in the account. How many dollars remain in the account?"""
    # Define Emma's starting account balance and daily spending
    account_balance = 100
    daily_spending = 8

    # Calculate Emma's ending account balance after 7 days
    ending_balance = account_balance - (daily_spending * 7)

    # Calculate the number of $5 bills Emma can get from the bank
    num_bills = ending_balance // 5

    # Calculate Emma's remaining account balance
    remaining_balance = ending_balance - (num_bills * 5)

    # Display Emma's remaining account balance
    result = remaining_balance
    return result

print(solution())