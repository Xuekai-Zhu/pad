def solution():
    
    land_cost = 30 * 20
    house_cost = 120000
    cow_cost = 20 * 1000
    chicken_cost = 100 * 5
    total_animal_cost = cow_cost + chicken_cost
    installation_cost = 6 * 100 + 6000
    total_cost = land_cost + house_cost + total_animal_cost + installation_cost
    result = total_cost
    return result

print(solution())