def solution():
    # Calculate the total number of cars
    total_cars = 6 + 12 + 2

    # Calculate the number of stations the train needs to pass through
    num_stations = total_cars / 6

    # Calculate the time it takes to travel between stations
    travel_time = 25 / 60  # convert to hours

    # Calculate the time it takes to unload at each station
    unload_time = 2 * 2 / 60 + 3 * 2 / 60 + 1 / 60  # convert to hours

    # Calculate the total time it takes to deliver all the cars
    total_time = num_stations * (travel_time + unload_time)

    # Convert to minutes and round to the nearest minute
    result = round(total_time * 60)

    return result

print(solution())