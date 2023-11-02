def solution():
    # Initialize the number of cars and the time elapsed
    coal_cars = 6
    iron_cars = 12
    wood_cars = 2
    time_elapsed = 0

    # Calculate the number of stations needed to deliver all the cars
    stations_needed = (coal_cars // 2) + (iron_cars // 3) + (wood_cars // 1)

    # Calculate the time needed to deliver all the cars
    time_needed = stations_needed * 25

    # Update the number of cars and time elapsed at each station
    for station in range(stations_needed):
        coal_cars -= min(coal_cars, 2)
        iron_cars -= min(iron_cars, 3)
        wood_cars -= min(wood_cars, 1)
        time_elapsed += 25

    result = time_elapsed
    return result

print(solution())