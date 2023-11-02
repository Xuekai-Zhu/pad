def solution():
    
    yellow_flowers = 10
    purple_flowers = yellow_flowers + (yellow_flowers * 0.80)
    green_flowers = (yellow_flowers + purple_flowers) * 0.25
    total_flowers = yellow_flowers + purple_flowers + green_flowers
    result = total_flowers
    return result

print(solution())