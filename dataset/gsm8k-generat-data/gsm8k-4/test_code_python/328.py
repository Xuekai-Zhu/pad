def solution():
    """A used car lot has 24 cars and motorcycles (in total) for sale. A third of the vehicles are motorcycles, and a quarter of the cars have a spare tire included. How many tires are on the used car lot’s vehicles in all?"""
    # Define the total number of vehicles
    total_vehicles = 24

    # Calculate the number of motorcycles
    motorcycles = total_vehicles // 3

    # Calculate the number of cars
    cars = total_vehicles - motorcycles

    # Calculate the number of cars with spare tires
    cars_with_spares = cars // 4

    # Calculate the number of tires
    total_tires = (motorcycles * 2) + (cars * 4) + (cars_with_spares * 1)

    result = total_tires
    return result

print(solution())