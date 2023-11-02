def solution():
    """An apartment complex has 4 identical buildings. Each building has 10 studio apartments, 20 2 person apartments, and 5 4 person apartments. How many people live in the apartment complex if it has 75% of its maximum occupancy?"""
    num_buildings = 4
    studio_apartments = 10
    two_person_apartments = 20
    four_person_apartments = 5
    max_occupancy = num_buildings * (studio_apartments + (2 * two_person_apartments) + (4 * four_person_apartments))
    occupancy_percentage = 0.75
    current_occupancy = occupancy_percentage * max_occupancy
    result = current_occupancy
    return result

print(solution())