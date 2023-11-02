def solution():
    
    glass_ice_cubes = 8
    pitcher_ice_cubes = 2 * glass_ice_cubes
    total_ice_cubes = glass_ice_cubes + pitcher_ice_cubes
    trays_needed = total_ice_cubes // 12 + (total_ice_cubes % 12 > 0)  
    result = trays_needed
    return result

print(solution())