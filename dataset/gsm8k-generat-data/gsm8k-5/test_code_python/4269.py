def solution():
    # Calculate the cost of the land
    land_cost = 30 * 20  # $20 per acre, 30 acres

    # Calculate the cost of the house
    house_cost = 120000

    # Calculate the cost of the cows
    cow_cost = 20 * 1000  # 20 cows, $1000 per cow

    # Calculate the cost of the chickens
    chicken_cost = 100 * 5  # 100 chickens, $5 per chicken

    # Calculate the cost of the solar panels
    solar_installation_cost = 6 * 100  # $100 per hour, 6 hours of installation
    solar_equipment_cost = 6000
    solar_cost = solar_installation_cost + solar_equipment_cost

    # Calculate the total cost
    total_cost = land_cost + house_cost + cow_cost + chicken_cost + solar_cost
    result = total_cost
    return result

print(solution())