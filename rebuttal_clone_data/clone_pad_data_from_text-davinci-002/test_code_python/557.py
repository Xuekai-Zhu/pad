def solution():
    total_plants = 18
    total_tomatoes = total_plants * 7
    dried_tomatoes = total_tomatoes / 2
    tomatoes_for_sauce = (total_tomatoes - dried_tomatoes) / 3
    tomatoes_left = total_tomatoes - dried_tomatoes - tomatoes_for_sauce
    result = tomatoes_left
    
    return result

print(solution())