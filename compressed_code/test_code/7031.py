def solution():
    
    total_rows = 6
    flowers_per_row = 13
    total_flowers = total_rows * flowers_per_row
    yellow_flowers = 12
    green_flowers = 2 * yellow_flowers
    red_flowers = total_flowers - yellow_flowers - green_flowers
    result = red_flowers
    return result

print(solution())