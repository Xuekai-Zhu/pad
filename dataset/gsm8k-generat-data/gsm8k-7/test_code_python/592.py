def solution():
    fuel_rate = 5 # liters of fuel per km
    trip1_distance = 30 # km
    trip2_distance = 20 # km

    # Calculate the total distance of both trips
    total_distance = trip1_distance + trip2_distance

    # Calculate the total amount of fuel needed for both trips
    total_fuel = fuel_rate * total_distance
    result = total_fuel
    return result

print(solution())