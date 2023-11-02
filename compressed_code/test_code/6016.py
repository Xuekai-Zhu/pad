def solution():
    
    corn_water = 20
    cotton_water = 80
    beans_water = corn_water * 2
    bob_water = (3 * corn_water) + (9 * cotton_water) + (12 * beans_water)
    brenda_water = (6 * corn_water) + (7 * cotton_water) + (14 * beans_water)
    bernie_water = (2 * corn_water) + (12 * cotton_water)
    total_water = bob_water + brenda_water + bernie_water
    bob_percent = (bob_water / total_water) * 100
    result = bob_percent
    return result

print(solution())