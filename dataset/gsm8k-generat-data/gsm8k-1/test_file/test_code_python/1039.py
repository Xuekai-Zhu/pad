def solution():
    """There are 26 countries in South America and, in each country, there are 5 cities with 1000 people living in each city. If the whole population lives in these cities, how many people are there in South America?"""
    countries = 26
    cities_per_country = 5
    population_per_city = 1000
    total_population = countries * cities_per_country * population_per_city
    result = total_population
    return result

print(solution())