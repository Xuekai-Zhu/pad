def solution():
    
    bean_seedlings = 64
    pumpkin_seeds = 84
    radishes = 48
    bean_rows = bean_seedlings / 8
    pumpkin_rows = pumpkin_seeds / 7
    radish_rows = radishes / 6
    total_rows = bean_rows + pumpkin_rows + radish_rows
    plant_beds = total_rows / 2
    result = plant_beds
    return result

print(solution())