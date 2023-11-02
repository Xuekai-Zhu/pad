def solution():
     gallons_per_day = 1.5
     quarts_per_gallon = 4
     quarts_per_day = gallons_per_day * quarts_per_gallon
     quarts_per_week = quarts_per_day * 7
     result = quarts_per_week
     return result

print(solution())