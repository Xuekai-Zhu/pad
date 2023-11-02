def solution():
    initial_land = 300
    cost_per_sq_meter = 20
    land1_cost = 8000
    land2_cost = 4000

    # Calculate the total cost of both lands
    total_land_cost = land1_cost + land2_cost

    # Calculate the total area of the land bought
    total_land_area = total_land_cost / cost_per_sq_meter

    # Calculate the total area of Carlson's land after buying the new land
    total_area = initial_land + total_land_area
    result = total_area
    return result

print(solution())