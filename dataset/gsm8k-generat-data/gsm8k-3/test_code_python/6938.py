def solution():
    """A train leaves its departure station with 6 coal cars, 12 iron cars, and 2 wood cars. Between each station, there are 6 miles, and it takes 25 minutes to travel between them. At each station, the train can deposit up to 2 coal cars, 3 iron cars, and 1 wood car. How many minutes will it take to deliver all the cars?"""
    # Define the number of initial cars
    coal_cars = 6
    iron_cars = 12
    wood_cars = 2

    # Define the maximum number of cars that can be deposited at each station
    max_coal_deposits = 2
    max_iron_deposits = 3
    max_wood_deposits = 1

    # Define the distance between stations in miles and the time it takes to travel between them in minutes
    distance_between_stations = 6
    time_between_stations = 25

    # Initialize the total time to 0
    total_time = 0

    # Loop through each station until all the cars have been delivered
    while coal_cars > 0 or iron_cars > 0 or wood_cars > 0:
        # Calculate the number of cars to deposit at this station
        coal_deposits = min(coal_cars, max_coal_deposits)
        iron_deposits = min(iron_cars, max_iron_deposits)
        wood_deposits = min(wood_cars, max_wood_deposits)

        # Update the number of cars on the train and add the travel time to the total time
        coal_cars -= coal_deposits
        iron_cars -= iron_deposits
        wood_cars -= wood_deposits
        total_time += time_between_stations

    # Display the total time in minutes
    result = total_time
    return result

print(solution())