def solution():
    """John has 3 bedroom doors and two outside doors to replace. The outside doors cost $20 each to replace and the bedroom doors are half that cost. How much does he pay in total?"""
    # Define the cost of the outside doors and the bedroom doors
    outside_door_cost = 20
    bedroom_door_cost = outside_door_cost / 2

    # Define the number of outside doors and bedroom doors to replace
    num_outside_doors = 2
    num_bedroom_doors = 3

    # Calculate the total cost of replacing all the doors
    total_cost = (outside_door_cost * num_outside_doors) + (bedroom_door_cost * num_bedroom_doors)

    result = total_cost
    return result

print(solution())