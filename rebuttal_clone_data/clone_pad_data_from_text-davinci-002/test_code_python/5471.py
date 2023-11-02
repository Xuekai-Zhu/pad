def solution():
    Diana_situps_per_minute = 4
    Hani_situps_per_minute = Diana_situps_per_minute + 3
    Diana_situps = Diana_situps_per_minute * 40
    Hani_situps = Hani_situps_per_minute * 40
    total_situps = Diana_situps + Hani_situps
    result = total_situps
    return result

print(solution())