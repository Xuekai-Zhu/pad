def solution():
    
    flowers_per_color = 125
    total_flowers = (flowers_per_color - 45) + (flowers_per_color - 61) + (flowers_per_color - 30) + (flowers_per_color - 40)
    bouquets = total_flowers // 9
    result = bouquets
    return result

print(solution())