def solution():
    
    total_plants = 80
    percent_flowering = 40
    flowering_plants = total_plants * (percent_flowering / 100)
    porch_plants = flowering_plants / 4
    flowers_per_plant = 5
    total_flowers = porch_plants * flowers_per_plant
    result = total_flowers
    return result

print(solution())