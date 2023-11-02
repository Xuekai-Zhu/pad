def solution():
    num_countries = 26
    num_cities = 5
    population_per_city = 1000

    # Calculate the total population of all cities
    total_population = num_countries * num_cities * population_per_city

    # Calculate the number of people in South America
    num_south_america = total_population / 2
    result = num_south_america
    return result

print(solution())