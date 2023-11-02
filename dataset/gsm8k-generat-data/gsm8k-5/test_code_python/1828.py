def solution():
    initial_investment = 1000  # Joseph initially invests $1000
    monthly_deposit = 100  # Joseph adds $100 to his investment every month
    interest_rate = 0.1  # The hedge fund promises a yearly interest rate of 10%
    time_years = 2  # Joseph wants to know how much money he will have after 2 years
    time_months = time_years * 12  # Convert the time to months

    # Calculate the total amount of money Joseph will have after 2 years
    total_amount = initial_investment
    for i in range(time_months):
        total_amount += monthly_deposit
        total_amount *= (1 + (interest_rate/12))

    result = total_amount
    return result

print(solution())