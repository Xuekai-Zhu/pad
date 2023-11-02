def solution():
    
    orange_flowers = 10
    red_flowers = 2 * orange_flowers
    yellow_flowers = red_flowers - 5
    total_flowers = 105
    pink_purple_flowers = (total_flowers - orange_flowers - red_flowers - yellow_flowers) / 2
    result = pink_purple_flowers
    return result

print(solution())