def solution():
    initial_fuel = 3000  # initial fuel in the tank
    remaining_fuel = 180  # fuel remaining on January 1, 2006
    filled_fuel = 3000 - remaining_fuel  # fuel filled on January 1, 2006
    final_fuel = 1238  # fuel remaining on May 1, 2006

    # Calculate the fuel used between November 1, 2005 and May 1, 2006
    fuel_used = initial_fuel - remaining_fuel + filled_fuel - final_fuel
    result = fuel_used
    return result

print(solution())