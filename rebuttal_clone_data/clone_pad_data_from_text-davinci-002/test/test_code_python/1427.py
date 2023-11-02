def solution():
     indoor_tables = 9
     outdoor_tables = 11
     chairs_per_indoor_table = 10
     chairs_per_outdoor_table = 3
     total_chairs = (indoor_tables * chairs_per_indoor_table) + (outdoor_tables * chairs_per_outdoor_table)
     result = total_chairs
     return result

print(solution())