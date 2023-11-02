def solution():
    # Calculate the total number of toy cars Olaf received
    grandpa_cars = 2 * uncle_cars
    dad_cars = 10
    mum_cars = dad_cars + 5
    auntie_cars = uncle_cars + 1
    total_received = grandpa_cars + dad_cars + mum_cars + auntie_cars

    # Calculate the total number of toy cars Olaf has after receiving the gifts
    total_cars = 150 + total_received
    result = total_cars
    return result

print(solution())