def solution():
    # Calculate the total number of solar systems in the galaxy
    solar_systems = 20 * 8
    # Calculate the total number of planets and solar systems in the galaxy
    total_objects = 20 + solar_systems
    result = (solar_systems, total_objects)
    return result

print(solution())