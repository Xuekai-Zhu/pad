def solution():
    """Karen is packing her backpack for a long-distance hike. She packs 20 pounds of water, 10 pounds of food, and 20 pounds of gear. During her hike, she drinks 2 pounds of water per hour and eats 1/3rd the weight of food per hour as water per hour. How much weight is she carrying after six hours?"""
    # Define the initial weight of Karen's backpack
    initial_weight = 50 # 20 pounds water + 10 pounds food + 20 pounds gear

    # Define the weight of water Karen drinks per hour
    water_per_hour = 2

    # Define the weight of food Karen eats per hour
    food_per_hour = water_per_hour / 3

    # Calculate the total weight of water Karen drinks during the hike
    water_weight = water_per_hour * 6

    # Calculate the total weight of food Karen eats during the hike
    food_weight = food_per_hour * 6

    # Calculate the total weight of Karen's backpack after 6 hours
    total_weight = initial_weight - water_weight - food_weight

    # Display the total weight
    result = total_weight
    return result

print(solution())