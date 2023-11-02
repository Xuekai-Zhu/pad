def solution():
     rows_of_chairs = 40
     chairs_per_row = 20
     empty_chairs = 10
     total_chairs = rows_of_chairs * chairs_per_row
     occupied_chairs = total_chairs - empty_chairs
     result = occupied_chairs
     return result

print(solution())