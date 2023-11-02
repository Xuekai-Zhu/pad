def solution():
    
    base_chance = 10
    base_height = 66
    height_increase = 10
    devin_height = 65 + 3
    height_difference = devin_height - base_height
    chance_increase = (height_difference * height_increase)
    final_chance = base_chance + chance_increase
    result = final_chance
    return result

print(solution())