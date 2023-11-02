def solution():
    asking_price = 5200
    maintenance_cost = asking_price * 0.1
    offer1 = asking_price - maintenance_cost

    headlights_cost = 80
    tires_cost = 3 * headlights_cost
    offer2 = asking_price - headlights_cost - tires_cost

    difference = offer1 - offer2
    result = difference
    return result

print(solution())