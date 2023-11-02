def solution():
    asking_price = 5200
    inspection_cost = asking_price / 10
    headlights_cost = 80
    tires_cost = 3 * headlights_cost

    # First offer calculation
    if_buyer1 = asking_price + inspection_cost

    # Second offer calculation
    if_buyer2 = asking_price - headlights_cost - tires_cost

    # Difference between the two offers
    difference = if_buyer1 - if_buyer2
    result = difference
    return result

print(solution())