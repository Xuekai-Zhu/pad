def solution():
    
    total_flowers = 10
    red_flowers = 4
    white_flowers = 2
    blue_flowers = total_flowers - red_flowers - white_flowers
    blue_percentage = (blue_flowers / total_flowers) * 100
    result = blue_percentage
    return result

print(solution())