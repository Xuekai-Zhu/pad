def solution():
    """In a city, the number of people living per cubic yard is 80. How many more people are in a city with 9000 cubic yards than a city with 6400 cubic yards?"""
    # Define the population density per cubic yard
    POP_DENSITY = 80

    # Define the volume of the first city
    volume1 = 6400

    # Define the volume of the second city
    volume2 = 9000

    # Calculate the population of the first city
    population1 = POP_DENSITY * volume1

    # Calculate the population of the second city
    population2 = POP_DENSITY * volume2

    # Calculate the difference in populations
    population_diff = population2 - population1

    # Display the difference in populations
    result = population_diff
    return result

print(solution())