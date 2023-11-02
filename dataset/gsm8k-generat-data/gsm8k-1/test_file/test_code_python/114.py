def solution():
    """A customs officer at the main port of SeaSide clearances counted 2 containers of imported vehicles, each having 5 vehicles inside.
    The next day, more containers were brought in, and the total number of vehicles at the port became 30.
    Calculate the number of containers that were imported on the second day, assuming all the containers contain 5 vehicles."""
    initial_containers = 2
    initial_vehicles = initial_containers * 5
    total_vehicles = 30
    second_day_vehicles = total_vehicles - initial_vehicles
    second_day_containers = second_day_vehicles / 5
    result = second_day_containers
    return result

print(solution())