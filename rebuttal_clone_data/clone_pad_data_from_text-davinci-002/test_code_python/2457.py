def solution():
     bees_per_day = 1200
     initial_population = 80000
     remaining_population = initial_population / 4
     days_to_die = remaining_population / bees_per_day
     result = days_to_die
     return result

print(solution())