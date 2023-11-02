def solution():
    """The price of electricity went up by 25%. John's old computer used 800 watts and his new computer uses 50% more. If the old price of electricity was 12 cents per kilowatt-hour, how much does his computer cost, in dollars, to run for 50 hours?"""
    # Define the old price of electricity and the cost of running John's old computer
    OLD_ELECTRICITY_PRICE = 0.12
    OLD_COMPUTER_WATTS = 800
    OLD_COMPUTER_HOURS = 50

    old_computer_kwh = (OLD_COMPUTER_WATTS/1000) * OLD_COMPUTER_HOURS
    old_computer_cost = old_computer_kwh * OLD_ELECTRICITY_PRICE

    # Define the new wattage of John's computer
    NEW_COMPUTER_WATTS = OLD_COMPUTER_WATTS * 1.5

    # Calculate the cost of running John's new computer for 50 hours
    NEW_COMPUTER_HOURS = 50

    new_computer_kwh = (NEW_COMPUTER_WATTS/1000) * NEW_COMPUTER_HOURS
    new_computer_cost = new_computer_kwh * (OLD_ELECTRICITY_PRICE * 1.25)

    # Calculate the difference in cost between John's old and new computers
    cost_difference = new_computer_cost - old_computer_cost

    # return the result
    result = round(cost_difference, 2)
    return result

print(solution())