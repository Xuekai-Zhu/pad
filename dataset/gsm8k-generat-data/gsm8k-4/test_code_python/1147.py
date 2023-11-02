def solution():
    """In a city, the number of people living per cubic yard is 80. How many more people are in a city with 9000 cubic yards than a city with 6400 cubic yards?"""
    # Define the population density per cubic yard
    density = 80

    # Calculate the number of people in the city with 9000 cubic yards
    city_1_population = density * 9000

    # Calculate the number of people in the city with 6400 cubic yards
    city_2_population = density * 6400

    # Calculate the difference in population between the two cities
    population_difference = city_1_population - city_2_population

    # return the result
    result = population_difference
    return result

print(solution())