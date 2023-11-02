def solution():
    num_bedroom_doors = 3  # John has 3 bedroom doors to replace
    cost_bedroom_door = 10  # Each bedroom door costs half the amount of an outside door
    num_outside_doors = 2  # John has 2 outside doors to replace
    cost_outside_door = 20  # Each outside door costs $20 to replace

    # Calculate the total cost of replacing the bedroom doors
    total_cost_bedroom_doors = num_bedroom_doors * cost_bedroom_door

    # Calculate the total cost of replacing the outside doors
    total_cost_outside_doors = num_outside_doors * cost_outside_door

    # Calculate the total cost by adding together the cost of the bedroom doors and outside doors
    total_cost = total_cost_bedroom_doors + total_cost_outside_doors
    result = total_cost
    return result

print(solution())