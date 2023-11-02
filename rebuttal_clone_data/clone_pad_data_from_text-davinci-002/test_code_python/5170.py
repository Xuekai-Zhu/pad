def solution():
    water_liters = 20
    vinegar_liters = 18
    water_percentage = 3/5
    vinegar_percentage = 5/6
    water_used = water_liters * water_percentage
    vinegar_used = vinegar_liters * vinegar_percentage
    total_liters = water_used + vinegar_used
    result = total_liters
    return result

print(solution())