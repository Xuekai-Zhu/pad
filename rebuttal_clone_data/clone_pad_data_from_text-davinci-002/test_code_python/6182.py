def solution():
     round_tables = 2
     rectangular_tables = 2
     chairs_per_round_table = 6
     chairs_per_rectangular_table = 7
     total_chairs = (round_tables * chairs_per_round_table) + (rectangular_tables * chairs_per_rectangular_table)
     result = total_chairs
     return result

print(solution())