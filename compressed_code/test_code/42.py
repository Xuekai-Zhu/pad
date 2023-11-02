def solution():
    
    living_room = 4 * 6
    bedroom = 2 * 4
    total_curtains = living_room + bedroom
    total_fabric = 16 * 12
    remaining_fabric = total_fabric - total_curtains
    result = remaining_fabric
    return result

print(solution())