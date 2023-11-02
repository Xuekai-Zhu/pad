def solution():
    
    servings = 12
    chicken_weight = 4.5
    stuffing_weight = 24
    total_weight = chicken_weight + (stuffing_weight / 16)  
    weight_per_serving = total_weight / servings
    ounces_per_serving = weight_per_serving * 16  
    result = ounces_per_serving
    return result

print(solution())