def solution():
    
    
    diana_situp_rate = 4
    hani_situp_rate = diana_situp_rate + 3
    diana_situps = 40
    hani_situps = hani_situp_rate * (diana_situps / diana_situp_rate)
    total_situps = diana_situps + hani_situps
    
    result = total_situps
    return result

print(solution())