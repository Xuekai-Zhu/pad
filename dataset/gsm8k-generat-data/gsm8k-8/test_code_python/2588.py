def solution():
    # Define the cost of an outside door
    outside_door_cost = 20

    # Define the cost of a bedroom door
    bedroom_door_cost = outside_door_cost / 2

    # Calculate the total cost of the outside doors
    total_outside_door_cost = outside_door_cost * 2

    # Calculate the total cost of the bedroom doors
    total_bedroom_door_cost = bedroom_door_cost * 3

    # Calculate the total cost of all the doors
    total_door_cost = total_outside_door_cost + total_bedroom_door_cost
    result = total_door_cost
    return result

print(solution())