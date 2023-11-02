def solution():
    """Today, at the school science lesson, Jake learned that there are 8 more solar systems for every planet in the galaxy. If there are 20 planets in the galaxy, how many solar systems and planets are there altogether?"""
    # Define the number of planets in the galaxy
    planets = 20

    # Calculate the number of solar systems in the galaxy
    solar_systems = planets * 8

    # Calculate the total number of planets and solar systems
    total = planets + solar_systems

    # Return the result as a tuple
    result = (total, planets + solar_systems)
    return result

print(solution())