def solution():
    
    rows = 50
    flowers_per_row = 400
    total_flowers = rows * flowers_per_row
    cut_percent = 60
    remaining_flowers = total_flowers * (100 - cut_percent) / 100
    result = remaining_flowers
    return result

print(solution())