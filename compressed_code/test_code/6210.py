def solution():
    
    plants = 18
    tomatoes_per_plant = 7
    total_tomatoes = plants * tomatoes_per_plant
    dried_tomatoes = total_tomatoes / 2
    remaining_tomatoes = total_tomatoes - dried_tomatoes
    marinara_tomatoes = remaining_tomatoes / 3
    remaining_tomatoes -= marinara_tomatoes
    result = remaining_tomatoes
    return result

print(solution())