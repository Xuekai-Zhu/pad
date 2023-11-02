def solution():
    
    
    salons = [
        {'name': "Gustran Salon", 'haircut': 45, 'facial_cleaning': 22, 'nails': 30},
        {'name': "Barbara's Shop", 'haircut': 30, 'facial_cleaning': 28, 'nails': 40},
        {'name': "The Fancy Salon", 'haircut': 34, 'facial_cleaning': 30, 'nails': 20}
    ]
    
    cheapest_price = float('inf')
    
    for salon in salons:
        total_price = salon['haircut'] + salon['facial_cleaning'] + salon['nails']
        if total_price < cheapest_price:
            cheapest_price = total_price
    
    result = cheapest_price
    return result

print(solution())