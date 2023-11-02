def solution():
    
    fire_type = 30
    grass_type = 20
    water_type = 40
    lost_growth = 8
    bought_grass_type = 14
    total_growth = lost_growth + bought_grass_type
    total_cards = fire_type + grass_type + total_growth
    probability = (total_cards / total_growth) * 100
    result = probability
    return result

print(solution())