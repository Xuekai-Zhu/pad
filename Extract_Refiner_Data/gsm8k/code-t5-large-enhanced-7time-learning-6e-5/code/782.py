def solution():
    
    tomato_plants = 5
    eggplant_plants = 8
    tomatoes_per_plant = 22
    eggplants_per_plant = 4
    total_tomatoes = tomato_plants * tomatoes_per_plant
    total_eggplants = eggplant_plants * eggplants_per_plant
    total_fruits = total_tomatoes + total_eggplants
    result = total_fruits
    return result

print(solution())