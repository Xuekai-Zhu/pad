def solution():
    # Calculate the total number of apartments in the block
    apartments_per_floor = [6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5]  # half of the floors have 6 apartments and the other half have 5 apartments
    total_apartments = sum(apartments_per_floor)  # add up the number of apartments on each floor

    # Calculate the maximum number of residents that can live in the block
    max_residents = total_apartments * 4  # each apartment can accommodate a maximum of 4 residents
    result = max_residents
    return result

print(solution())