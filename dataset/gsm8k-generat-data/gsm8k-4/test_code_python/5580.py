def solution():
    """Jude is trading his bottle cap collection to Arthur for some of Arthur's matchbox vehicles. Arthur charges Jude 5 bottle caps for a car and 6 bottle caps for a truck. Jude has 100 bottle caps. If he buys 10 trucks and spends 75% of his remaining bottle caps on cars, how many total matchbox vehicles does he buy?"""
    # Define the prices of a car and a truck in terms of bottle caps
    CAR_PRICE = 5
    TRUCK_PRICE = 6

    # Define the number of bottle caps Jude has
    bottle_caps = 100

    # Calculate the number of trucks Jude can buy
    trucks_bought = 10

    # Subtract the cost of the trucks from the total number of bottle caps
    bottle_caps -= trucks_bought * TRUCK_PRICE

    # Calculate the number of bottle caps Jude has left
    bottle_caps_left = bottle_caps

    # Calculate the number of cars Jude can buy with 75% of his remaining bottle caps
    cars_bought = (bottle_caps_left * 0.75) // CAR_PRICE

    # Calculate the total number of vehicles Jude buys
    total_vehicles = trucks_bought + cars_bought

    result = total_vehicles
    return result

print(solution())