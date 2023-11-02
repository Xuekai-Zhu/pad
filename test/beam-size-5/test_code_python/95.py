def solution():
    
    initial_plants = 18
    windowledges = 40
    plants_per_ledge = 2
    plants_given_away = 1
    total_plants = initial_plants + (windowledges * plants_per_ledge)
    remaining_plants = total_plants - plants_given_away
    result = remaining_plants
    return result

print(solution())