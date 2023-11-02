def solution():
    """A Moroccan restaurant received 3 different shipments of couscous. The first two shipments of 7 and 13 pounds arrived on the same day. The next day's shipment was 45 pounds of couscous. If it takes 5 pounds of couscous to make a dish, how many dishes did the restaurant make?"""
    shipment_1 = 7
    shipment_2 = 13
    shipment_3 = 45
    couscous_per_dish = 5
    total_couscous = shipment_1 + shipment_2 + shipment_3
    total_dishes = total_couscous // couscous_per_dish
    result = total_dishes
    return result

print(solution())