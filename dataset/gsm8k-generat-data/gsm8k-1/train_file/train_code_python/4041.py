def solution():
    """Carlson bought land that cost $8000 and additional land that cost $4000. He initially owned 300 square meters of land. If the land he bought costs $20 per square meter, how big is his land after buying the new land?"""
    initial_land = 300
    land_cost = 20
    land1_cost = 8000
    land2_cost = 4000
    land1_size = land1_cost / land_cost
    land2_size = land2_cost / land_cost
    total_land = initial_land + land1_size + land2_size
    result = total_land
    return result

print(solution())