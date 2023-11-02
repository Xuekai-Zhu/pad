def solution():
    """Steve has a bank account that earns 10% interest every year. He puts $100 in it, and then 10 each year. How much money is in it after two years?"""
    # Define initial variables
    principal = 100
    annual_contrib = 10
    annual_interest_rate = 0.1
    years = 2

    # Calculate the future value of the account after two years
    future_value = principal + annual_contrib
    future_value *= (1 + annual_interest_rate)
    future_value += annual_contrib
    future_value *= (1 + annual_interest_rate)

    # Display the final value of the account
    result = future_value
    return result

print(solution())