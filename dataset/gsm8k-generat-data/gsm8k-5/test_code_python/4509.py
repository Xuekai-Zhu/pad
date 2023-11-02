def solution():
    num_buildings = 4  # The apartment complex has 4 identical buildings
    num_studio_apts = 10  # Each building has 10 studio apartments
    num_2person_apts = 20  # Each building has 20 2 person apartments
    num_4person_apts = 5  # Each building has 5 4 person apartments

    # Calculate the maximum number of residents in the complex
    max_residents = num_buildings * (num_studio_apts + (2 * num_2person_apts) + (4 * num_4person_apts))

    # Calculate the current number of residents, based on 75% occupancy
    current_residents = max_residents * 0.75

    result = current_residents
    return result

print(solution())