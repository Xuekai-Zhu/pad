def solution():
    land_acres = 30
    land_price_per_acre = 20
    house_cost = 120000
    num_cows = 20
    cow_cost = 1000
    num_chickens = 100
    chicken_cost = 5
    solar_panel_install_time = 6
    solar_panel_install_cost_per_hour = 100
    solar_panel_equipment_cost = 6000

    # Calculate the total cost of the land
    land_cost = land_acres * land_price_per_acre

    # Calculate the total cost of the cows
    cow_cost_total = num_cows * cow_cost

    # Calculate the total cost of the chickens
    chicken_cost_total = num_chickens * chicken_cost

    # Calculate the total cost of the solar panels
    solar_panel_installation_cost = solar_panel_install_time * solar_panel_install_cost_per_hour
    solar_panel_total_cost = solar_panel_installation_cost + solar_panel_equipment_cost

    # Calculate the total cost of everything
    total_cost = land_cost + house_cost + cow_cost_total + chicken_cost_total + solar_panel_total_cost
    result = total_cost
    return result

print(solution())