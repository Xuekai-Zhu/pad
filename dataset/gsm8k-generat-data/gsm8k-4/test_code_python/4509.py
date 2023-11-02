def solution():
    """An apartment complex has 4 identical buildings. Each building has 10 studio apartments, 20 2 person apartments, and 5 4 person apartments. How many people live in the apartment complex if it has 75% of its maximum occupancy?"""
    # Define the number of buildings
    num_buildings = 4

    # Define the number of apartments in each category
    num_studio = 10
    num_2person = 20
    num_4person = 5

    # Calculate the maximum occupancy of each building
    max_occ_per_building = num_studio + (num_2person * 2) + (num_4person * 4)

    # Calculate the maximum occupancy of the entire complex
    max_occupancy = max_occ_per_building * num_buildings

    # Calculate the current occupancy based on the given percentage
    current_occupancy = max_occupancy * 0.75

    # Calculate the number of people living in the apartment complex
    num_people = current_occupancy * 1.5   # assuming an average of 1.5 people per apartment

    result = num_people
    return result

print(solution())