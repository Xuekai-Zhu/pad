def solution():
    """An apartment building has 12 floors and half of them are full. The remaining floors are all at half-capacity. If each floor has 10 apartments and each apartment has four people, how many people are in the building?"""
    # Define the number of floors and apartments per floor
    FLOORS = 12
    APARTMENTS_PER_FLOOR = 10

    # Calculate the total number of apartments and people on full floors
    full_floors = FLOORS // 2
    full_apartments = full_floors * APARTMENTS_PER_FLOOR
    full_people = full_apartments * 4

    # Calculate the total number of apartments and people on half-capacity floors
    half_capacity_floors = FLOORS - full_floors
    half_capacity_apartments = half_capacity_floors * APARTMENTS_PER_FLOOR // 2
    half_capacity_people = half_capacity_apartments * 4

    # Calculate the total number of people in the building
    total_people = full_people + half_capacity_people

    # Display the total number of people
    result = total_people
    return result

print(solution())