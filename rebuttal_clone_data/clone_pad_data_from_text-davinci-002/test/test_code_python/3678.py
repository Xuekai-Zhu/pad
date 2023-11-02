def solution():
     days_per_year = 250 
     seasons_per_year = 5
     seasons_on_planet = 3
     days_on_planet = seasons_on_planet * (days_per_year / seasons_per_year)
     result = days_on_planet
     return result

print(solution())