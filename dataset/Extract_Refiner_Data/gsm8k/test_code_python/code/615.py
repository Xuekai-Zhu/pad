def solution():
    
    # Define the number of street lights per pole and the number of poles per intersection
    STREET_LIGHTS_PER_POT = 4
    poles_per_intersection = 6

    # Calculate the total number of street lights
    total_streetlights = STREET_LIGHTS_PER_POT * 4 * 4

    # Calculate the number of streetlights not working
    non_working_streetlights = 20

    # Calculate the number of streetlights working
    working_streetlights = total_streetlights - non_working_streetlights

    # Calculate the number of functioning street lights
    functioning_streetlights = working_streetlights

    # Display the number of functioning street lights
    result = functioning_streetlights
    return result

print(solution())