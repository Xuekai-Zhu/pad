def solution():
    # Define the population density in people per cubic yard
    population_density = 80

    # Calculate the number of people in the city with 9000 cubic yards
    city1_population = population_density * 9000

    # Calculate the number of people in the city with 6400 cubic yards
    city2_population = population_density * 6400

    # Calculate the difference in population between the two cities
    population_difference = city1_population - city2_population
    result = population_difference
    return result

print(solution())