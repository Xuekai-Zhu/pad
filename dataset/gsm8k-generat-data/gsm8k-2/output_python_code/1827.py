def solution():
    """Joseph invested $1000 into a hedge fund. The fund promised a yearly interest rate of 10%. If he deposited an additional $100 every month into the account to add to his initial investment of $1000, how much money will he have in the fund after two years?"""
    principal = 1000
    monthly_deposit = 100
    annual_interest = 0.1
    time_years = 2
    time_months = time_years * 12

    for i in range(time_months):
        principal += monthly_deposit
        monthly_interest = (principal * annual_interest) / 12
        principal += monthly_interest

    result = principal
    return result

print(solution())