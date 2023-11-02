def solution():
    # Calculate the number of motorcycles and cars
    total_vehicles = 24
    motorcycles = total_vehicles/3
    cars = total_vehicles - motorcycles

    # Calculate the number of cars with a spare tire
    cars_with_spare_tires = cars/4

    # Calculate the total number of tires on the lot's vehicles
    total_tires = (motorcycles*2) + (cars*4) + (cars_with_spare_tires*1)

    result = total_tires
    return result

print(solution())