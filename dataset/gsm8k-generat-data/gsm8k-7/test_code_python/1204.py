def solution():
    num_planets = 20
    num_solar_systems_per_planet = 8

    # Calculate the total number of solar systems in the galaxy
    num_solar_systems = num_planets * num_solar_systems_per_planet

    # Calculate the total number of planets and solar systems in the galaxy
    total_objects = num_planets + num_solar_systems
    result = total_objects
    return result

print(solution())