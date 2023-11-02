def solution():
    # Calculate the total number of apartments in the building
    total_apartments = 12 * 10  # 12 floors with 10 apartments per floor

    # Calculate the number of full floors in the building
    full_floors = 12 // 2  # half of the floors are full, so there are 6 full floors

    # Calculate the number of people in the full floors
    full_floor_people = full_floors * 10 * 4  # each apartment has 4 people

    # Calculate the number of remaining floors
    remaining_floors = 12 - full_floors

    # Calculate the number of people in the remaining floors
    remaining_floor_people = remaining_floors * 10 * 4 * 0.5  # each remaining floor is at half-capacity

    # Calculate the total number of people in the building
    total_people = full_floor_people + remaining_floor_people

    result = total_people
    return result

print(solution())