def solution():
    """Joseph invested $1000 into a hedge fund. The fund promised a yearly interest rate of 10%. If he deposited an additional $100 every month into the account to add to his initial investment of $1000, how much money will he have in the fund after two years?"""
    # Define the initial investment amount and the monthly deposit amount
    initial_investment = 1000
    monthly_deposit = 100

    # Calculate the yearly interest rate and the number of compounding periods per year
    yearly_interest_rate = 0.1
    compounding_periods = 12

    # Calculate the total number of compounding periods over two years
    total_periods = 2 * compounding_periods

    # Calculate the total amount of money Joseph will have in the fund after two years
    balance = initial_investment
    for i in range(total_periods):
        # Add the monthly deposit to the balance
        balance += monthly_deposit

        # Calculate the interest earned in this period and add it to the balance
        interest_earned = balance * (yearly_interest_rate / compounding_periods)
        balance += interest_earned

    result = balance
    return result

print(solution())