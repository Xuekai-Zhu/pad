def solution():
    initial_collection = 150  # Olaf's initial collection consisted of 150 cars

    # Calculate the number of toy cars given by each family member
    grandpa_cars = 2 * uncle_cars
    dad_cars = mum_cars - 5
    auntie_cars = uncle_cars + 1

    # Calculate the total number of toy cars given to Olaf
    total_cars = grandpa_cars + dad_cars + auntie_cars + 10

    # Calculate the total number of toy cars in Olaf's collection after receiving gifts
    total_collection = initial_collection + total_cars
    result = total_collection
    return result

print(solution())