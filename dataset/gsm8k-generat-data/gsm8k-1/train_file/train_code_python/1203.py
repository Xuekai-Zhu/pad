def solution():
    """Today, at the school science lesson, Jake learned that there are 8 more solar systems for every planet in the galaxy. If there are 20 planets in the galaxy, how many solar systems and planets are there altogether?"""
    planets = 20
    solar_systems = planets * 8 + planets
    total = planets + solar_systems
    result = total
    return result

print(solution())