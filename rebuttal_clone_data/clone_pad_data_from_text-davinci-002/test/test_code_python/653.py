def solution():
    people_per_cubic_yard = 80
    city_1_cubic_yards = 9000
    city_2_cubic_yards = 6400
    city_1_population = city_1_cubic_yards * people_per_cubic_yard
    city_2_population = city_2_cubic_yards * people_per_cubic_yard
    difference = city_1_population - city_2_population
    result = difference
    return result

print(solution())