def solution():
    total_vehicles = 24  # The used car lot has 24 vehicles in total

    # Calculate the number of motorcycles and cars
    motorcycles = total_vehicles / 3
    cars = total_vehicles - motorcycles

    # Calculate the number of cars with a spare tire
    cars_with_spare_tire = cars / 4

    # Calculate the total number of tires on the used car lot's vehicles
    total_tires = (motorcycles * 2) + (cars * 4) + (cars_with_spare_tire * 1)

    result = total_tires
    return result

print(solution())