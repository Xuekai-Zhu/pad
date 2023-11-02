def solution():
    indoor_tables = 8
    outdoor_tables = 12
    chairs_per_indoor_table = 3
    chairs_per_outdoor_table = 3
    total_chairs = (indoor_tables * chairs_per_indoor_table) + (outdoor_tables * chairs_per_outdoor_table)
    result = total_chairs
    return result

print(solution())