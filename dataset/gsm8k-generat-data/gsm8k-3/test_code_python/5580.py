def solution():
    """Jude is trading his bottle cap collection to Arthur for some of Arthur's matchbox vehicles. Arthur charges Jude 5 bottle caps for a car and 6 bottle caps for a truck. Jude has 100 bottle caps. If he buys 10 trucks and spends 75% of his remaining bottle caps on cars, how many total matchbox vehicles does he buy?"""
    # Define the cost of each type of matchbox vehicle in terms of bottle caps
    CAR_COST = 5
    TRUCK_COST = 6

    # Define the number of bottle caps Jude has
    bottle_caps = 100

    # Calculate the total cost of the trucks
    truck_cost = 10 * TRUCK_COST

    # Subtract the cost of the trucks from the total number of bottle caps Jude has
    remaining_bottle_caps = bottle_caps - truck_cost

    # Calculate the number of bottle caps Jude can spend on cars
    car_caps = remaining_bottle_caps * 0.75

    # Calculate the number of cars Jude can buy
    num_cars = int(car_caps / CAR_COST)

    # Calculate the total number of matchbox vehicles Jude buys
    total_vehicles = num_cars + 10

    # Display the total number of matchbox vehicles
    result = total_vehicles
    return result

print(solution())