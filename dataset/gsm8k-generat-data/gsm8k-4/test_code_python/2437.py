def solution():
    """Emma's bank account has $100 in it. Each day of the week, she spends $8. At the end of the week, she goes to the bank and asks for as many $5 bills as her account can give her. She leaves the rest in the account. How many dollars remain in the account?"""
    # Define the initial balance and the amount spent each day
    balance = 100
    daily_spending = 8
    
    # Calculate the balance after a week of spending
    balance = balance - (daily_spending * 7)
    
    # Calculate the number of $5 bills that can be withdrawn from the balance
    num_bills = balance // 5
    
    # Calculate the remaining amount in the account
    remaining_balance = balance - (num_bills * 5)

    result = remaining_balance
    return result

print(solution())