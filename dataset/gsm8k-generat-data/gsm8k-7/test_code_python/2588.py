def solution():
    num_bedroom_doors = 3
    bedroom_door_cost = 10  # half the cost of outside doors
    num_outside_doors = 2
    outside_door_cost = 20

    # Calculate the total cost of all bedroom doors
    total_bedroom_door_cost = num_bedroom_doors * bedroom_door_cost

    # Calculate the total cost of all outside doors
    total_outside_door_cost = num_outside_doors * outside_door_cost

    # Calculate the total cost of all doors
    total_cost = total_bedroom_door_cost + total_outside_door_cost
    result = total_cost
    return result

print(solution())