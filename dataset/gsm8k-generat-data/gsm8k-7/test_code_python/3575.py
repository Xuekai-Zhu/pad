def solution():
    num_floors = 12
    full_floors = num_floors // 2
    half_capacity_floors = num_floors - full_floors

    # Calculate the number of people on the full floors
    full_floor_people = full_floors * 10 * 4

    # Calculate the number of people on the half-capacity floors
    half_capacity_people = half_capacity_floors * 10 * 2 * 4

    # Calculate the total number of people in the building
    total_people = full_floor_people + half_capacity_people
    result = total_people
    return result

print(solution())