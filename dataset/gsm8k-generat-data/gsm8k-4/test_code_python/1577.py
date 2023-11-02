def solution():
    """Steve has a bank account that earns 10% interest every year. He puts $100 in it, and then 10 each year. How much money is in it after two years?"""
    # Define the initial deposit and annual contribution
    initial_deposit = 100
    annual_contribution = 10

    # Define the interest rate and number of years
    interest_rate = 0.1
    years = 2

    # Calculate the final balance with compound interest
    balance = initial_deposit + annual_contribution
    for year in range(1, years+1):
        balance = balance * (1 + interest_rate) + annual_contribution

    # return the result
    result = round(balance, 2)
    return result

print(solution())