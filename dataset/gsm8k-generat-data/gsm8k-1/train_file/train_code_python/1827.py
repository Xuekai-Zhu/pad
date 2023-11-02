def solution():
    """Joseph invested $1000 into a hedge fund. The fund promised a yearly interest rate of 10%. If he deposited an additional $100 every month into the account to add to his initial investment of $1000, how much money will he have in the fund after two years?"""
    initial_investment = 1000
    monthly_deposit = 100
    yearly_interest_rate = 0.10
    months_in_two_years = 24
    current_balance = initial_investment
    for i in range(months_in_two_years):
        current_balance += monthly_deposit
        monthly_interest = (current_balance * yearly_interest_rate) / 12
        current_balance += monthly_interest
    result = current_balance
    return result

print(solution())