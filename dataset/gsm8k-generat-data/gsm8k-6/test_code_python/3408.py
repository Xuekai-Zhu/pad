def solution():
    # Calculate the new wattage of John's computer
    new_wattage = 800 * 1.5  # 50% more than the old computer

    # Calculate the new price of electricity per kilowatt-hour
    new_price = 0.12 * 1.25  # price increased by 25%

    # Calculate the total kilowatt-hours used by the computer
    kilowatt_hours = (new_wattage / 1000) * 50  # watts to kilowatts, multiply by hours

    # Calculate the total cost of running the computer for 50 hours
    total_cost = kilowatt_hours * new_price

    result = total_cost
    return result

print(solution())