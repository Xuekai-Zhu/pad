def solution():
    total_floors = 12  # The block has 12 floors
    half_floors = total_floors / 2  # Half of the floors have 6 apartments and the other half has 5
    apartments_on_half_floors = half_floors * (6 + 5)  # Total number of apartments on half the floors
    total_apartments = apartments_on_half_floors * 2  # Total number of apartments in the block
    max_residents = total_apartments * 4  # Each apartment can accommodate a maximum of 4 residents
    result = max_residents
    return result

print(solution())