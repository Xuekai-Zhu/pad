def solution():
     cars_per_month = 100
     target_cars_per_year = 1800
     additional_cars_per_month = (target_cars_per_year - (cars_per_month * 12)) / 12
     result = additional_cars_per_month
     return result

print(solution())