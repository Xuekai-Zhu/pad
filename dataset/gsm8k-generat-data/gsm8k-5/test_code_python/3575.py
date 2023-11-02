def solution():
    # Determine the number of full floors
    full_floors = 12 / 2

    # Determine the number of half-capacity floors
    half_floors = full_floors

    # Determine the total number of apartments
    total_apartments = (full_floors * 10) + (half_floors * 5)

    # Determine the total number of people
    total_people = total_apartments * 4
    result = total_people
    return result

print(solution())