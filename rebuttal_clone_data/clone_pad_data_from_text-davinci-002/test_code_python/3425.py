def solution():
     population = 4000
     growth_factor = 3
     predicted_increase = 40
     current_population = population * growth_factor
     predicted_population = current_population + (current_population * (predicted_increase/100))
     result = predicted_population
     return result

print(solution())