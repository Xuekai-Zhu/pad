def solution():
    """In the city, there is a block of flats. This block has 12 floors. Half of the floors have 6 apartments and the other half have 5 apartments. One apartment can accommodate a maximum of 4 residents. What is the maximum number of residents that can live in this block of flats?"""
    num_floors = 12
    num_apartments_per_floor = [6 if i < num_floors/2 else 5 for i in range(num_floors)]
    max_residents_per_apartment = 4
    total_residents = sum(num_apartments_per_floor) * max_residents_per_apartment
    result = total_residents
    return result

print(solution())