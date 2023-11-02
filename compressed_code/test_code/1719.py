def solution():
    
    tomato_plants = 6
    eggplant_plants = 2
    pepper_plants = 4

    
    tomato_plants_remaining = tomato_plants // 2
    pepper_plants_remaining = pepper_plants - 1

    
    total_vegetables = (tomato_plants_remaining + eggplant_plants + pepper_plants_remaining) * 7

    result = total_vegetables
    return result

print(solution())