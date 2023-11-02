def solution():
    # Define the cost of the bike and Zach's current savings
    bike_cost = 100
    current_savings = 65

    # Calculate Zach's earnings for the week
    weekly_earnings = 5 + 10 + 7 * 2  # allowance + lawn mowing + babysitting

    # Calculate the total amount Zach will have after the week's earnings
    total_savings = current_savings + weekly_earnings

    # Calculate how much more money Zach needs to save to buy the bike
    remaining_cost = bike_cost - total_savings
    result = remaining_cost
    return result

print(solution())