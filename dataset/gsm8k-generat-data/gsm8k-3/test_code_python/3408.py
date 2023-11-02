def solution():
    """The price of electricity went up by 25%.  John's old computer used 800 watts and his new computer uses 50% more.  If the old price of electricity was 12 cents per kilowatt-hour, how much does his computer cost, in dollars, to run for 50 hours?"""
    # Define the old cost of electricity per kilowatt-hour and the wattage of John's old computer
    OLD_ELECTRICITY_PRICE = 0.12
    OLD_COMPUTER_WATTAGE = 800

    # Calculate the new wattage of John's computer
    NEW_COMPUTER_WATTAGE = OLD_COMPUTER_WATTAGE * 1.5

    # Calculate the new cost of electricity per kilowatt-hour
    NEW_ELECTRICITY_PRICE = OLD_ELECTRICITY_PRICE * 1.25

    # Calculate the total kilowatt-hours used by John's computer for 50 hours
    kilowatt_hours = NEW_COMPUTER_WATTAGE * 50 / 1000

    # Calculate the total cost of running John's computer for 50 hours
    total_cost = kilowatt_hours * NEW_ELECTRICITY_PRICE

    # Display the total cost
    result = total_cost
    return result

print(solution())