def solution():
    
    indoor_tables = 8
    outdoor_tables = 12
    chairs_per_table = 3
    total_chairs = (indoor_tables * chairs_per_table) + (outdoor_tables * chairs_per_table)
    result = total_chairs
    return result

print(solution())