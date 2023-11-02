def solution():
    """An apartment complex has 4 identical buildings. Each building has 10 studio apartments, 20 2 person apartments, and 5 4 person apartments. How many people live in the apartment complex if it has 75% of its maximum occupancy?"""
    # Define the number of apartments in each building
    STUDIO_APARTMENTS = 10
    TWO_PERSON_APARTMENTS = 20
    FOUR_PERSON_APARTMENTS = 5
    # Define the maximum occupancy per building
    MAX_OCCUPANCY = STUDIO_APARTMENTS + (TWO_PERSON_APARTMENTS * 2) + (FOUR_PERSON_APARTMENTS * 4)
    # Define the number of buildings in the complex
    NUM_BUILDINGS = 4
    # Calculate the maximum occupancy of the entire complex
    MAX_OCCUPANCY_COMPLEX = MAX_OCCUPANCY * NUM_BUILDINGS
    # Calculate the actual occupancy based on 75% occupancy
    actual_occupancy = 0.75 * MAX_OCCUPANCY_COMPLEX
    # Display the actual occupancy
    result = actual_occupancy
    return result

print(solution())