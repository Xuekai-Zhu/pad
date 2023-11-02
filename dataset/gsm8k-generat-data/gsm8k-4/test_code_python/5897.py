def solution():
    """Olaf collects colorful toy cars. At first, his collection consisted of 150 cars. His family, knowing his hobby, decided to give him some toy cars. Grandpa gave Olaf twice as many toy cars as the uncle. Dad gave Olaf 10 toy cars, 5 less than Mum. Auntie gave Olaf 6 toy cars, 1 more than the uncle. How many toy cars does Olaf have in total, after receiving all these gifts?"""
    
    # Define the initial number of toy cars and the gifts received from each family member
    initial_cars = 150
    grandpa_cars = None
    uncle_cars = None
    dad_cars = None
    mum_cars = None
    auntie_cars = None
    
    # Calculate the number of toy cars received from Grandpa and Uncle
    uncle_cars = 2
    grandpa_cars = uncle_cars * 2
    
    # Calculate the number of toy cars received from Dad and Mum
    mum_cars = 15
    dad_cars = mum_cars - 5
    
    # Calculate the number of toy cars received from Auntie
    auntie_cars = uncle_cars + 1
    
    # Calculate the total number of toy cars after receiving all the gifts
    total_cars = initial_cars + grandpa_cars + uncle_cars + dad_cars + mum_cars + auntie_cars
    
    # return the result
    result = total_cars
    return result

print(solution())