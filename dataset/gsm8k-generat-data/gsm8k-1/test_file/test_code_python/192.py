def solution():
    """200 pounds of carrots are to be distributed to 40 restaurants in a certain city. Each restaurant is to receive 2 pounds of carrots. How many pounds of carrots will not be used?"""
    total_carrots = 200
    num_restaurants = 40
    carrots_per_restaurant = 2
    total_carrots_used = num_restaurants * carrots_per_restaurant
    leftover_carrots = total_carrots - total_carrots_used
    result = leftover_carrots
    return result

print(solution())