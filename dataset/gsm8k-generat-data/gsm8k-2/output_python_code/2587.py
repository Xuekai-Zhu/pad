def solution():
    """John has 3 bedroom doors and two outside doors to replace. The outside doors cost $20 each to replace and the bedroom doors are half that cost. How much does he pay in total?"""
    num_bedroom_doors = 3
    num_outside_doors = 2
    outside_door_cost = 20
    bedroom_door_cost = outside_door_cost / 2
    total_cost = (num_bedroom_doors * bedroom_door_cost) + (num_outside_doors * outside_door_cost)
    result = total_cost
    return result

print(solution())