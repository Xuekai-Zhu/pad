def solution():
    
    pencils_per_day = 100
    days_per_week = 5
    starting_pencils = 80
    total_pencils_made = pencils_per_day * days_per_week
    remaining_pencils = total_pencils_made + starting_pencils - 350
    result = remaining_pencils
    return result

print(solution())