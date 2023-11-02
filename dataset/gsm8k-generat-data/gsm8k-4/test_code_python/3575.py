def solution():
    """An apartment building has 12 floors and half of them are full. The remaining floors are all at half-capacity. If each floor has 10 apartments and each apartment has four people, how many people are in the building?"""
    # Define the number of floors and apartments per floor
    floors = 12
    full_floors = floors // 2
    half_cap_floors = floors - full_floors

    # Calculate the number of people in full floors
    full_people = full_floors * 10 * 4

    # Calculate the number of people in half-capacity floors
    half_people = half_cap_floors * 10 * 4 * 0.5

    # Calculate the total number of people in the building
    total_people = full_people + half_people

    # Return the result
    result = total_people
    return result

print(solution())