def solution():
    fuel_per_km = 5  # John uses 5 liters of fuel per km
    trip1_distance = 30  # First trip is 30 km
    trip2_distance = 20  # Second trip is 20 km

    # Calculate the total distance traveled
    total_distance = trip1_distance + trip2_distance

    # Calculate the total fuel needed for the trip
    total_fuel = total_distance * fuel_per_km
    result = total_fuel
    return result

print(solution())