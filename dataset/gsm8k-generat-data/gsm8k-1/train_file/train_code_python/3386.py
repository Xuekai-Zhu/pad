def solution():
    """Bryan bought three different bottles of milk. The bottles contain the following volumes of milk: 2 liters, 750 milliliters, 250 milliliters. How many liters of milk did Bryan buy in total?"""
    liters_1 = 2
    liters_2 = 0.75
    liters_3 = 0.25
    total_liters = liters_1 + (liters_2 / 1000) + (liters_3 / 1000)
    result = total_liters
    return result

print(solution())