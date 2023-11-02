def solution():
    """Haily wants to go to the salon and do her nails, cut her hair and do a facial cleaning. She called 3 salons to get their prices: Gustran Salon, Barbara's Shop, and The Fancy Salon. At Gustran Salon, the haircut is $45, the facial cleaning is $22 and the nails are $30. At Barbara's shop, the nails are $40, the haircut is $30 and the facial cleaning is $28. And, at the Fancy Salon, the facial cleaning is $30, the haircut is $34 and the nails are $20. How much would she spend at the cheapest salon?"""
    
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