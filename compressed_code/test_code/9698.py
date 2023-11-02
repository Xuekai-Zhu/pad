def solution():
    
    violets_water_per_hour = 800
    dogs_water_per_hour = 400
    total_water_per_hour = violets_water_per_hour + dogs_water_per_hour
    max_hours = (4.8 * 1000) / total_water_per_hour
    result = max_hours
    return result

print(solution())