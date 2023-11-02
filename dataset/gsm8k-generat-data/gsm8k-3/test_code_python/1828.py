def solution():
    """Joseph invested $1000 into a hedge fund. The fund promised a yearly interest rate of 10%. If he deposited an additional $100 every month into the account to add to his initial investment of $1000, how much money will he have in the fund after two years?"""
    # Define the initial investment and monthly deposit amount
    initial_investment = 1000
    monthly_deposit = 100

    # Define the interest rate and number of years
    interest_rate = 0.1
    num_years = 2

    # Calculate the total number of months
    num_months = num_years * 12

    # Calculate the final amount in the fund
    final_amount = initial_investment
    for i in range(num_months):
        final_amount += monthly_deposit
        monthly_interest = (final_amount * interest_rate) / 12
        final_amount += monthly_interest

    # Display the final amount in the fund
    result = final_amount
    return result

print(solution())