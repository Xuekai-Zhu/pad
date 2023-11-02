def solution():
     gallons_per_jug = 0.5
     cups_per_gallon = 16
     days_per_jug = 4
     cups_per_day = (gallons_per_jug * cups_per_gallon) / days_per_jug
     result = cups_per_day
     return result

print(solution())