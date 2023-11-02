def solution():
    """Toms car gets 50 miles to the gallon. He drives 75 miles per day. If gas is $3 per gallon how much does he spend on gas in 10 days?"""
    # Define the car's gas efficiency in miles per gallon
    mpg = 50

    # Define the daily distance driven
    daily_distance = 75

    # Calculate the daily gas consumption in gallons
    daily_gas_consumption = daily_distance / mpg

    # Calculate the daily cost of gas
    daily_gas_cost = daily_gas_consumption * 3

    # Calculate the total cost of gas over 10 days
    total_gas_cost = daily_gas_cost * 10

    # return the result
    result = total_gas_cost
    return result

print(solution())