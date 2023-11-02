def solution():
    """A train leaves its departure station with 6 coal cars, 12 iron cars, and 2 wood cars. Between each station, there are 6 miles, and it takes 25 minutes to travel between them. At each station, the train can deposit up to 2 coal cars, 3 iron cars, and 1 wood car. How many minutes will it take to deliver all the cars?"""
    # Define the number of coal, iron, and wood cars initially on the train
    coal_cars = 6
    iron_cars = 12
    wood_cars = 2

    # Define the maximum number of cars that can be deposited at each station
    max_coal = 2
    max_iron = 3
    max_wood = 1

    # Define the travel distance and time between each station
    distance = 6
    travel_time = 25

    # Initialize the total travel time
    total_time = 0

    # Calculate the number of stations required to deliver all the cars
    max_stations = max(coal_cars // max_coal, iron_cars // max_iron, wood_cars // max_wood)

    # Deliver the cars at each station, until all the cars have been delivered
    for station in range(1, max_stations+1):
        # Calculate the number of cars to be deposited at this station
        coal_to_deposit = min(coal_cars, max_coal)
        iron_to_deposit = min(iron_cars, max_iron)
        wood_to_deposit = min(wood_cars, max_wood)

        # Update the number of cars on the train
        coal_cars -= coal_to_deposit
        iron_cars -= iron_to_deposit
        wood_cars -= wood_to_deposit

        # Calculate the travel time to this station
        station_time = distance * travel_time

        # Add the station time to the total travel time
        total_time += station_time

    # return the total travel time
    result = total_time
    return result

print(solution())