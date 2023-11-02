def solution():
    """Ricardo grows tomatoes and eggplants in his garden. Each tomato plant yields 22 tomatoes while each plant of eggplant yields 4 eggplants. He planted 5 tomato plants and 8 plants of eggplant. How many fruits can Ricardo get from his plants?"""
    tomatoes_per_plant = 22
    eggplants_per_plant = 4
    num_tomato_plants = 5
    num_eggplant_plants = 8
    total_tomatoes = tomatoes_per_plant * num_tomato_plants
    total_eggplants = eggplants_per_plant * num_eggplant_plants
    total_fruits = total_tomatoes + total_eggplants
    result = total_fruits
    return result

print(solution())