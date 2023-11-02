def solution():
    """Emma's bank account has $100 in it. Each day of the week, she spends $8. At the end of the week, she goes to the bank and asks for as many $5 bills as her account can give her. She leaves the rest in the account. How many dollars remain in the account?"""
    starting_amount = 100
    daily_spending = 8
    remaining_amount = starting_amount - (daily_spending * 7)
    bills = remaining_amount // 5
    remaining_balance = remaining_amount - (bills * 5)
    result = remaining_balance
    return result

print(solution())