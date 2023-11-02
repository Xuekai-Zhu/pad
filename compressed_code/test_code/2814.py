def solution():
    
    num_buildings = 2
    num_floors = 12
    num_apts_per_floor = 6
    num_doors_per_apt = 7
    total_doors = num_buildings * num_floors * num_apts_per_floor * num_doors_per_apt
    result = total_doors
    return result

print(solution())