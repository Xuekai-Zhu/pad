def solution():
    # Calculate the cost of the land
    land_cost = 30 * 20

    # Calculate the cost of the house
    house_cost = 120000

    # Calculate the cost of the cows
    cow_cost = 20 * 1000

    # Calculate the cost of the chickens
    chicken_cost = 100 * 5

    # Calculate the cost of the solar panels
    solar_panel_installation_cost = 6 * 100
    solar_panel_equipment_cost = 6000
    solar_panel_cost = solar_panel_installation_cost + solar_panel_equipment_cost

    # Calculate the total cost
    total_cost = land_cost + house_cost + cow_cost + chicken_cost + solar_panel_cost
    result = total_cost
    return result

print(solution())