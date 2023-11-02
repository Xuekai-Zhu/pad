def solution():
    """Olaf collects colorful toy cars. At first, his collection consisted of 150 cars. His family, knowing his hobby, decided to give him some toy cars. Grandpa gave Olaf twice as many toy cars as the uncle. Dad gave Olaf 10 toy cars, 5 less than Mum. Auntie gave Olaf 6 toy cars, 1 more than the uncle. How many toy cars does Olaf have in total, after receiving all these gifts?"""
    # Define the initial number of cars and the number of cars each family member gave
    initial_cars = 150
    grandpa_cars = 2 * uncle_cars
    dad_cars = 10
    mum_cars = dad_cars + 5
    auntie_cars = uncle_cars + 1

    # Calculate the total number of cars after receiving the gifts
    total_cars = initial_cars + grandpa_cars + dad_cars + mum_cars + auntie_cars

    # Display the total number of cars
    result = total_cars
    return result

print(solution())