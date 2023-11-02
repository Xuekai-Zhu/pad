def solution():
    """Olaf collects colorful toy cars. At first, his collection consisted of 150 cars. His family, knowing his hobby, decided to give him some toy cars. Grandpa gave Olaf twice as many toy cars as the uncle. Dad gave Olaf 10 toy cars, 5 less than Mum. Auntie gave Olaf 6 toy cars, 1 more than the uncle. How many toy cars does Olaf have in total, after receiving all these gifts?"""
    initial_cars = 150
    grandpa_cars = 2 * uncle_cars
    uncle_cars = auntie_cars - 1
    auntie_cars = dad_cars + 6
    dad_cars = mum_cars - 5
    mum_cars = 10 + dad_cars + auntie_cars + uncle_cars + grandpa_cars
    total_cars = initial_cars + mum_cars

    result = total_cars
    return result

print(solution())