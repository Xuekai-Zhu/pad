def solution():
    # Calculate the volume of air needed to fill each tire
    air_per_tire = 500
    air_needed_tire1 = air_per_tire
    air_needed_tire2 = air_per_tire
    air_needed_tire3 = 0.6 * air_per_tire
    air_needed_tire4 = 0.3 * air_per_tire

    # Calculate the total volume of air needed
    total_air_needed = air_needed_tire1 + air_needed_tire2 + air_needed_tire3 + air_needed_tire4

    # Calculate the number of pumps needed to fill all tires
    pumps_needed = total_air_needed / 50
    result = pumps_needed
    return result

print(solution())