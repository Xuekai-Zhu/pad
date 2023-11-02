def solution():
    initial_fuel = 3000  # The initial fuel tank had 3,000 liters
    fuel_remaining_Jan1 = 180  # On Jan 1st, there were 180 liters remaining
    fuel_used_first_period = initial_fuel - fuel_remaining_Jan1  # This is the fuel used from Nov 1st to Jan 1st

    # Calculate the fuel used from Jan 1st to May 1st
    fuel_used_second_period = initial_fuel - 1238

    # Total fuel used between Nov 1st and May 1st
    total_fuel_used = fuel_used_first_period + fuel_used_second_period
    result = total_fuel_used
    return result

print(solution())