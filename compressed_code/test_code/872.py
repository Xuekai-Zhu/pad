def solution():
    
    people_per_yard = 80
    city1_size = 6400
    city2_size = 9000
    city1_population = city1_size * people_per_yard
    city2_population = city2_size * people_per_yard
    difference = city2_population - city1_population
    result = difference
    return result

print(solution())