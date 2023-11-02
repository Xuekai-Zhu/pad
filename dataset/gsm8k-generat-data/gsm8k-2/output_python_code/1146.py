def solution():
    """In a city, the number of people living per cubic yard is 80. How many more people are in a city with 9000 cubic yards than a city with 6400 cubic yards?"""
    people_per_yard = 80
    city1_size = 6400
    city2_size = 9000
    city1_population = city1_size * people_per_yard
    city2_population = city2_size * people_per_yard
    difference = city2_population - city1_population
    result = difference
    return result

print(solution())