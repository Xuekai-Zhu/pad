def solution():
    shipment1_weight = 7
    shipment2_weight = 13
    shipment3_weight = 45
    couscous_per_dish = 5

    # Calculate the total weight of all shipments
    total_weight = shipment1_weight + shipment2_weight + shipment3_weight

    # Calculate the total number of dishes that can be made
    num_dishes = total_weight // couscous_per_dish
    result = num_dishes
    return result

print(solution())