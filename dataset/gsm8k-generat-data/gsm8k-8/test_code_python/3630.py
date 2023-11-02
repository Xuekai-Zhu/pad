def solution():
    # Define the number of floors and apartments per building
    floors_per_building = 12
    apartments_per_floor = 6

    # Calculate the total number of apartments
    total_apartments = floors_per_building * apartments_per_floor * 2

    # Calculate the total number of doors needed
    total_doors_needed = total_apartments * 7

    result = total_doors_needed
    return result

print(solution())