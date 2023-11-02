def solution():
    num_stories = 25
    apartments_per_floor = 4
    occupants_per_apartment = 2

    # Calculate the total number of floors
    total_floors = num_stories

    # Calculate the total number of apartments in the building
    total_apartments = total_floors * apartments_per_floor

    # Calculate the total number of occupants in the building
    total_occupants = total_apartments * occupants_per_apartment
    result = total_occupants
    return result

print(solution())