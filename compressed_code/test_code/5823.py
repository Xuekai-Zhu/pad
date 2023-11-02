def solution():
    
    living_room = 4 * 6
    bedroom = 2 * 4
    total_used = living_room + bedroom
    bolt_of_fabric = 16 * 12
    remaining_fabric = bolt_of_fabric - total_used
    result = remaining_fabric
    return result

print(solution())