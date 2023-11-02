def solution():
    """A used car lot has 24 cars and motorcycles (in total) for sale. A third of the vehicles are motorcycles, and a quarter of the cars have a spare tire included. How many tires are on the used car lot’s vehicles in all?"""
    # Calculate the number of motorcycles and cars
    total_vehicles = 24
    motorcycles = total_vehicles // 3
    cars = total_vehicles - motorcycles

    # Calculate the number of cars with spare tires
    cars_with_spares = cars // 4

    # Calculate the total number of tires
    motorcycle_tires = motorcycles * 2
    car_tires = (cars - cars_with_spares) * 4 + cars_with_spares * 5

    total_tires = motorcycle_tires + car_tires

    # Display the total number of tires
    result = total_tires
    return result

print(solution())