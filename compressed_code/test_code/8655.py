def solution():
    
    num_buildings = 2
    num_floors = 12
    apartments_per_floor = 6
    doors_per_apartment = 7
    num_apartments = num_floors * apartments_per_floor * num_buildings
    num_doors = num_apartments * doors_per_apartment
    result = num_doors
    return result

print(solution())