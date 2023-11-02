def solution():
    num_floors = 12
    half_floors = num_floors // 2

    # Calculate the total number of apartments on each type of floor
    num_apartments_1 = half_floors * 6
    num_apartments_2 = half_floors * 5

    # Calculate the maximum number of residents in each type of apartment
    max_residents_1 = 4
    max_residents_2 = 4

    # Calculate the maximum number of residents in the entire block of flats
    max_residents = (num_apartments_1 * max_residents_1) + (num_apartments_2 * max_residents_2)
    result = max_residents
    return result

print(solution())