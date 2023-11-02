def solution():
    
    tomatoes_per_plant = 22
    eggplants_per_plant = 4
    planted_tomatoes = 5
    planted_eggplants = 8
    total_tomatoes = tomatoes_per_plant * planted_tomatoes
    total_eggplants = eggplants_per_plant * planted_eggplants
    total_fruits = total_tomatoes + total_eggplants
    result = total_fruits
    return result

print(solution())