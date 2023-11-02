def solution():
    # Calculate the cost of replacing the outside doors
    outside_door_cost = 20 * 2

    # Calculate the cost of replacing the bedroom doors
    bedroom_door_cost = (1/2) * outside_door_cost * 3

    # Calculate the total cost
    total_cost = outside_door_cost + bedroom_door_cost
    result = total_cost
    return result

print(solution())