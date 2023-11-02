def solution():
    
    total_flowers = 6 * 13
    yellow_flowers = 12
    green_flowers = 2 * yellow_flowers
    red_flowers = total_flowers - yellow_flowers - green_flowers
    result = red_flowers
    return result

print(solution())