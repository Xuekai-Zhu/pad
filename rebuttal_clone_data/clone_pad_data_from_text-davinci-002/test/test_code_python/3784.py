def solution():
    shipment1 = 7
    shipment2 = 13
    shipment3 = 45
    total_couscous = shipment1 + shipment2 + shipment3
    pounds_per_dish = 5
    total_dishes = total_couscous / pounds_per_dish
    result = total_dishes
    return result

print(solution())