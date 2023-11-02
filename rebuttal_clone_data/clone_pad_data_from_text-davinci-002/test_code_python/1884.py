def solution():
    sandbag_weight = 250
    sand_fraction = 0.8
    heavier_material_fraction = 1 - sand_fraction
    sandbag_weight_heavier_material = sandbag_weight * heavier_material_fraction
    sandbag_weight_sand = sandbag_weight * sand_fraction
    sand_density = 1
    heavier_material_density = 1.4
    sand_weight = sand_density * sandbag_weight_sand
    heavier_material_weight = heavier_material_density * sandbag_weight_heavier_material
    total_weight = sand_weight + heavier_material_weight
    result = total_weight
    
    return result

print(solution())