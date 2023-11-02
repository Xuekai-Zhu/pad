def solution():
    """In the city, there is a block of flats. This block has 12 floors. Half of the floors have 6 apartments and the other half have 5 apartments. One apartment can accommodate a maximum of 4 residents. What is the maximum number of residents that can live in this block of flats?"""
    # Define the number of floors and apartments
    floors = 12
    half_floors = floors // 2
    apartments_per_floor = [6] * half_floors + [5] * half_floors

    # Calculate the maximum number of residents
    max_residents = sum(apartments_per_floor) * 4

    result = max_residents
    return result

print(solution())