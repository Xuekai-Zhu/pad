def solution():
    num_buildings = 2
    num_floors = 12
    num_apartments_per_floor = 6
    num_doors_per_apartment = 7

    # Calculate the total number of floors in both buildings
    total_floors = num_floors * num_buildings

    # Calculate the total number of apartments in both buildings
    total_apartments = total_floors * num_apartments_per_floor

    # Calculate the total number of doors needed for all apartments
    total_doors_needed = total_apartments * num_doors_per_apartment
    result = total_doors_needed
    return result

print(solution())