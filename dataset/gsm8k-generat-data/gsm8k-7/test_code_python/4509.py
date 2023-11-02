def solution():
    num_buildings = 4
    num_studio = 10
    num_2_person = 20
    num_4_person = 5

    # Calculate the total number of apartments in the complex
    total_apartments = num_buildings * (num_studio + num_2_person + num_4_person)

    # Calculate the maximum occupancy of the complex
    max_occupancy = total_apartments * (1 + 2 + 4)

    # Calculate the number of people living in the complex at 75% occupancy
    num_people = max_occupancy * 0.75
    result = num_people
    return result

print(solution())