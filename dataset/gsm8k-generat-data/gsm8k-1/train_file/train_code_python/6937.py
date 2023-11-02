def solution():
    """A train leaves its departure station with 6 coal cars, 12 iron cars, and 2 wood cars. Between each station,
    there are 6 miles, and it takes 25 minutes to travel between them. At each station, the train can deposit up to
    2 coal cars, 3 iron cars, and 1 wood car. How many minutes will it take to deliver all the cars?"""
    coal_cars = 6
    iron_cars = 12
    wood_cars = 2
    miles_between_stations = 6
    time_between_stations = 25
    coal_deposited = 2
    iron_deposited = 3
    wood_deposited = 1

    while coal_cars != 0 or iron_cars != 0 or wood_cars != 0:
        if coal_cars > 0:
            coal_cars -= coal_deposited
        if iron_cars > 0:
            iron_cars -= iron_deposited
        if wood_cars > 0:
            wood_cars -= wood_deposited

        time_between_stations += 25

        if coal_cars < 0:
            coal_cars = 0
        if iron_cars < 0:
            iron_cars = 0
        if wood_cars < 0:
            wood_cars = 0

        coal_cars += coal_deposited
        iron_cars += iron_deposited
        wood_cars += wood_deposited

    result = time_between_stations
    return result

print(solution())