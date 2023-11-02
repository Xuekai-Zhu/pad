def solution():
    initial_fuel = 3000
    final_fuel = 1238
    remaining_fuel_on_jan_1 = 180

    # Calculate the fuel used from Nov 1 to Jan 1
    fuel_used_nov_to_jan = initial_fuel - remaining_fuel_on_jan_1

    # Calculate the fuel used from Jan 1 to May 1
    fuel_used_jan_to_may = final_fuel - initial_fuel

    # Total fuel used between Nov 1 and May 1
    total_fuel_used = fuel_used_nov_to_jan + fuel_used_jan_to_may

    result = total_fuel_used
    return result

print(solution())