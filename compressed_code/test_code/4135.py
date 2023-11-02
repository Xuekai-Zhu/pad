def solution():
    
    total_plants = 80
    flowering_plants = 0.4 * total_plants
    porch_plants = flowering_plants / 4
    flowers_per_plant = 5
    total_flowers = porch_plants * flowers_per_plant
    result = total_flowers
    return result

print(solution())