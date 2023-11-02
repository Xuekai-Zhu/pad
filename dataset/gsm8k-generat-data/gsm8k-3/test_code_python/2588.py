def solution():
    """John has 3 bedroom doors and two outside doors to replace.  The outside doors cost $20 each to replace and the bedroom doors are half that cost.  How much does he pay in total?"""
    # Define the cost of each type of door
    BEDROOM_DOOR_COST = 10
    OUTSIDE_DOOR_COST = 20

    # Define the number of each type of door to be replaced
    bedroom_doors = 3
    outside_doors = 2

    # Calculate the total cost of the bedroom doors
    bedroom_door_cost = bedroom_doors * BEDROOM_DOOR_COST

    # Calculate the total cost of the outside doors
    outside_door_cost = outside_doors * OUTSIDE_DOOR_COST

    # Calculate the total cost of all the doors
    total_cost = bedroom_door_cost + outside_door_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())