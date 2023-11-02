def solution():
    
    tomatoes_planted = 3 * 5
    cucumbers_planted = 5 * 4
    potatoes_planted = 30
    total_planted = tomatoes_planted + cucumbers_planted + potatoes_planted
    garden_capacity = 10 * 15
    more_can_plant = garden_capacity - total_planted
    result = more_can_plant
    return result

print(solution())