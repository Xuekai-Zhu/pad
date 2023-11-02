def solution():
    outside_doors = 2
    outside_door_cost = 20
    bedroom_doors = 3
    bedroom_door_cost = outside_door_cost / 2
    total_cost = (outside_doors * outside_door_cost) + (bedroom_doors * bedroom_door_cost)
    result = total_cost
    return result

print(solution())