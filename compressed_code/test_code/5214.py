def solution():
    
    shipment_1 = 7
    shipment_2 = 13
    shipment_3 = 45
    couscous_per_dish = 5
    total_couscous = shipment_1 + shipment_2 + shipment_3
    total_dishes = total_couscous // couscous_per_dish
    result = total_dishes
    return result

print(solution())