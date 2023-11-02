def solution():
    
    corn_rows = 10
    potato_rows = 5
    total_corn_cobs = corn_rows * 9
    total_potatoes = potato_rows * 30
    total_crops = total_corn_cobs + total_potatoes
    remaining_crops = total_crops * 0.5
    result = remaining_crops
    return result

print(solution())