def solution():
    crane1 = 228
    building1 = 200
    crane2 = 120
    building2 = 100
    crane3 = 147
    building3 = 140
    
    crane_height_total = crane1 + crane2 + crane3
    building_height_total = building1 + building2 + building3
    
    average_crane_height = crane_height_total / 3
    average_building_height = building_height_total / 3
    
    percentage = (average_crane_height - average_building_height) / average_building_height * 100
    
    result = percentage
    
    return result

print(solution())