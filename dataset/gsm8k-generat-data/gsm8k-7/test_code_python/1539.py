def solution():
    asking_price = 5200

    # First offer
    maintenance_inspection = asking_price / 10
    offer1 = asking_price + maintenance_inspection

    # Second offer
    headlights = 80
    tire_price = 3 * headlights
    offer2 = asking_price + headlights + tire_price

    # Difference between the two offers
    difference = offer2 - offer1
    result = difference
    return result

print(solution())