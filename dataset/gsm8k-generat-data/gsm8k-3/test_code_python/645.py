def solution():
    """In the city, there is a block of flats. This block has 12 floors. Half of the floors have 6 apartments and the other half have 5 apartments. One apartment can accommodate a maximum of 4 residents. What is the maximum number of residents that can live in this block of flats?"""
    # Calculate the number of floors with 6 apartments
    floors_with_6_apartments = 12 // 2

    # Calculate the number of floors with 5 apartments
    floors_with_5_apartments = 12 - floors_with_6_apartments

    # Calculate the maximum number of residents in each floor with 6 apartments
    max_residents_6_apartments = 6 * 4

    # Calculate the maximum number of residents in each floor with 5 apartments
    max_residents_5_apartments = 5 * 4

    # Calculate the maximum number of residents in the block of flats
    max_residents = (floors_with_6_apartments * max_residents_6_apartments) + (floors_with_5_apartments * max_residents_5_apartments)

    # Display the maximum number of residents
    result = max_residents
    return result

print(solution())