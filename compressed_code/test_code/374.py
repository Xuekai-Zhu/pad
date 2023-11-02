def solution():
    
    temp_drop = 32 - 8
    skid_chance = (temp_drop // 3) * 0.05
    control_chance = 0.4
    accident_chance = (1 - control_chance) * skid_chance
    result = accident_chance * 100
    return result

print(solution())