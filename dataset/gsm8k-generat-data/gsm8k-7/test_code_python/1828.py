def solution():
    initial_investment = 1000
    monthly_deposit = 100
    interest_rate = 0.1
    num_years = 2

    # Calculate the total number of months Joseph will be investing
    num_months = num_years * 12

    # Calculate the total amount invested after the given time period
    total_investment = initial_investment + (num_months * monthly_deposit)

    # Calculate the balance after taking into account the interest rate
    balance = total_investment * (1 + interest_rate)**num_years

    result = balance
    return result

print(solution())