def solution():
    
    tomato_plants = 6
    eggplant_plants = 2
    pepper_plants = 4

    
    lost_tomato_plants = tomato_plants / 2
    lost_pepper_plants = 1

    
    remaining_tomato_plants = tomato_plants - lost_tomato_plants
    remaining_pepper_plants = pepper_plants - lost_pepper_plants

    
    total_vegetables = (remaining_tomato_plants + eggplant_plants + remaining_pepper_plants) * 7

    result = total_vegetables
    return result

print(solution())