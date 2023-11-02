def solution():
    # Calculate the cost of Timothy's land purchase
    land_cost = 30 * 20

    # Calculate the cost of Timothy's house
    house_cost = 120000

    # Calculate the cost of Timothy's cows
    cow_cost = 20 * 1000

    # Calculate the cost of Timothy's chickens
    chicken_cost = 100 * 5

    # Calculate the cost of Timothy's solar panels
    solar_install_cost = 6 * 100
    solar_equipment_cost = 6000
    solar_total_cost = solar_install_cost + solar_equipment_cost

    # Calculate the total cost of Timothy's endeavors
    total_cost = land_cost + house_cost + cow_cost + chicken_cost + solar_total_cost
    result = total_cost
    return result

print(solution())