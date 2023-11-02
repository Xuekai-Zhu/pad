def solution():
    
    yellow_flowers = 10
    purple_flowers = yellow_flowers * 1.8
    total_flowers = yellow_flowers + purple_flowers
    green_flowers = total_flowers * 0.25
    total_flowers += green_flowers
    result = total_flowers
    return result

print(solution())