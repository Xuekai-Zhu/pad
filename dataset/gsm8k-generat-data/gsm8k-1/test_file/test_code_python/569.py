def solution():
    """Katina has $3000 in her savings account. If she removes $100 from the account every month, how much money will be remaining within the account after 2 years?"""
    starting_balance = 3000
    monthly_withdrawal = 100
    months_in_year = 12
    years = 2
    total_withdrawal = monthly_withdrawal * months_in_year * years
    ending_balance = starting_balance - total_withdrawal
    result = ending_balance
    return result

print(solution())