def solution():
    """Carlson bought land that cost $8000 and additional land that cost $4000. He initially owned 300 square meters of land. If the land he bought costs $20 per square meter, how big is his land after buying the new land?"""
    # Define the cost and size of each piece of land
    land1_cost = 8000
    land1_size = 0
    land2_cost = 4000
    land2_size = 0
    land_price = 20

    # Calculate the size of the first piece of land
    land1_size = land1_cost / land_price

    # Calculate the size of the second piece of land
    land2_size = land2_cost / land_price

    # Calculate the total size of the land
    total_size = land1_size + land2_size + 300

    # return the result
    result = total_size
    return result

print(solution())