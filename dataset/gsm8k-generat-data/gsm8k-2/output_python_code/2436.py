def solution():
    """Emma's bank account has $100 in it. Each day of the week, she spends $8. At the end of the week, she goes to the bank and asks for as many $5 bills as her account can give her. She leaves the rest in the account. How many dollars remain in the account?"""
    starting_balance = 100
    weekly_expenses = 7 * 8
    remaining_balance = starting_balance - weekly_expenses
    num_fives = remaining_balance // 5
    remaining_balance -= num_fives * 5
    result = remaining_balance
    return result

print(solution())