def solution():
    total_plants = 80
    flowering_plants = total_plants * (40 / 100)
    plants_on_porch = flowering_plants * (1 / 4)
    flowers_per_plant = 5
    total_flowers = plants_on_porch * flowers_per_plant
    result = total_flowers
    return result

print(solution())