def solution():
    total_distance = 100  # Sophia has traveled 100 miles
    fuel_needed = 4  # Sophia needed 4 gallons of gas to fill her tank
    tank_capacity = 12  # Sophia's car holds 12 gallons of gas

    # Calculate how many miles Sophia can drive on a single tank of gas
    miles_per_tank = (total_distance - fuel_needed) / tank_capacity
    result = miles_per_tank
    return result

print(solution())