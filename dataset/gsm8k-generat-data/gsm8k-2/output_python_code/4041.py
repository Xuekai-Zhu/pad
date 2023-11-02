def solution():
    """Carlson bought land that cost $8000 and additional land that cost $4000. He initially owned 300 square meters of land. If the land he bought costs $20 per square meter, how big is his land after buying the new land?"""
    land_cost = 20
    initial_land = 300
    bought_land_cost = 8000 + 4000
    bought_land_size = bought_land_cost / land_cost
    total_land_size = initial_land + bought_land_size
    result = total_land_size
    return result

print(solution())