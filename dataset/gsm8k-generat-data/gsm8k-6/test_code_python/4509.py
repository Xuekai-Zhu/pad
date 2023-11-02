def solution():
    # Calculate the total number of apartments in the complex
    total_apartments = 4 * (10 + 20 + 5)  # 4 buildings, each with 10 studio, 20 2-person, and 5 4-person apartments

    # Calculate the maximum occupancy of the complex in terms of people
    max_occupancy = total_apartments * (1 + 2*2 + 4*5)  # each apartment houses 1, 2, or 4 people

    # Calculate the number of people living in the apartment complex at 75% occupancy
    occupancy_75 = 0.75 * max_occupancy
    result = occupancy_75
    return result

print(solution())