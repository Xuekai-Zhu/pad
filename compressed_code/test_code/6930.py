def solution():
    
    garden1_plants = 20
    garden1_tomatoes = garden1_plants * 0.1
    garden2_plants = 15
    garden2_tomatoes = garden2_plants * (1/3)
    total_plants = garden1_plants + garden2_plants
    total_tomatoes = garden1_tomatoes + garden2_tomatoes
    percent_tomatoes = (total_tomatoes / total_plants) * 100
    result = percent_tomatoes
    return result

print(solution())