def solution():
    """Olaf collects colorful toy cars. At first, his collection consisted of 150 cars. His family, knowing his hobby, decided to give him some toy cars. Grandpa gave Olaf twice as many toy cars as the uncle. Dad gave Olaf 10 toy cars, 5 less than Mum. Auntie gave Olaf 6 toy cars, 1 more than the uncle. How many toy cars does Olaf have in total, after receiving all these gifts?"""
    base_collection = 150
    grandpa_gift = 2 * uncle_gift
    uncle_gift = 5
    dad_gift = 10
    mum_gift = dad_gift + 5
    auntie_gift = uncle_gift + 1
    
    total_gifts = grandpa_gift + uncle_gift + dad_gift + mum_gift + auntie_gift
    total_cars = base_collection + total_gifts
    result = total_cars
    return result

print(solution())