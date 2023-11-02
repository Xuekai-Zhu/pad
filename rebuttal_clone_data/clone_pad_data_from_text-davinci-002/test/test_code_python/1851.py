def solution():
     dog_food_per_meal = 1
     cups_per_bag = 32
     cups_per_day = dog_food_per_meal * 2
     days_per_bag = cups_per_bag / cups_per_day
     result = days_per_bag
     
     return result

print(solution())