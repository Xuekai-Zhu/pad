def solution():
    """An apartment complex has 4 identical buildings. Each building has 10 studio apartments, 20 2 person apartments, and 5 4 person apartments. How many people live in the apartment complex if it has 75% of its maximum occupancy?"""
    buildings = 4
    studios_per_building = 10
    two_person_apartments_per_building = 20
    four_person_apartments_per_building = 5
    occupancy_rate = 0.75
    
    total_studios = buildings * studios_per_building
    total_two_person_apartments = buildings * two_person_apartments_per_building
    total_four_person_apartments = buildings * four_person_apartments_per_building
    
    max_occupancy = (total_studios + (total_two_person_apartments * 2) + (total_four_person_apartments * 4))
    current_occupancy = max_occupancy * occupancy_rate
    
    result = current_occupancy
    return result

print(solution())