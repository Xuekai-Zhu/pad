def solution():
    
    diana_rate = 4
    diana_situps = 40
    hani_rate = diana_rate + 3
    hani_situps = hani_rate * (diana_situps / diana_rate)
    total_situps = diana_situps + hani_situps
    result = total_situps
    return result

print(solution())