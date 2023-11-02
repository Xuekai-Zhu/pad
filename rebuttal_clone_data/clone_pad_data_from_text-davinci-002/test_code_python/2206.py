def solution():
    tomato_plants = 6
    eggplant_plants = 2
    pepper_plants = 4
    dead_tomato_plants = tomato_plants / 2
    dead_pepper_plants = 1
    total_dead_plants = dead_tomato_plants + dead_pepper_plants
    total_plants = tomato_plants + eggplant_plants + pepper_plants
    total_alive_plants = total_plants - total_dead_plants
    vegetables_per_plant = 7
    total_vegetables = total_alive_plants * vegetables_per_plant
    result = total_vegetables
    return result

print(solution())