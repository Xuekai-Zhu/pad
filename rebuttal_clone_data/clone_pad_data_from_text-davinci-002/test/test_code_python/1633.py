def solution():
     minutes_per_brush = 2
     hours_per_day = 24
     days_brushed = 30
     minutes_brushed = minutes_per_brush * 3 * days_brushed
     hours_brushed = minutes_brushed / 60
     result = hours_brushed
     return result

print(solution())