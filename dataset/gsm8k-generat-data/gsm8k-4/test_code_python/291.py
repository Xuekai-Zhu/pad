def solution():
    """Mary used 15 gallons of fuel this week. Last week she used 20% less. How much fuel did she use in total for the two weeks?"""
    # Define the fuel used this week
    fuel_this_week = 15

    # Calculate the fuel used last week (20% less)
    fuel_last_week = fuel_this_week / 0.8 * 0.2

    # Calculate the total fuel used for both weeks
    total_fuel = fuel_this_week + fuel_last_week

    result = total_fuel
    return result

print(solution())