def solution():
     total_eggs = 24
     eggs_used = 2 + 4
     eggs_given_away = total_eggs - eggs_used
     meals = 3
     eggs_per_meal = eggs_given_away / meals
     result = eggs_per_meal
     return result

print(solution())