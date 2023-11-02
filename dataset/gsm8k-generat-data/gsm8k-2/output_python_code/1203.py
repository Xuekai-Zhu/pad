def solution():
    """Today, at the school science lesson, Jake learned that there are 8 more solar systems for every planet in the galaxy. If there are 20 planets in the galaxy, how many solar systems and planets are there altogether?"""
    num_planets = 20
    num_solar_systems = num_planets * 8
    total_objects = num_planets + num_solar_systems
    result = total_objects
    return result

print(solution())