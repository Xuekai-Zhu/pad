def solution():
    # Calculate the total number of floors
    total_floors = 12

    # Calculate the number of full floors
    full_floors = total_floors / 2

    # Calculate the number of half-capacity floors
    half_capacity_floors = total_floors - full_floors

    # Calculate the total number of apartments
    total_apartments = full_floors * 10 + half_capacity_floors * 5

    # Calculate the total number of people
    total_people = total_apartments * 4
    result = total_people
    return result

print(solution())