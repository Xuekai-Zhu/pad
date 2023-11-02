def solution():
    """Wendi lives on a plot of land that is 200 feet by 900 feet of grassland. She raises rabbits on her property by allowing the rabbits to graze on the grass that grows on her land. If one rabbit can eat enough grass to clear ten square yards of lawn area per day, and Wendi owns 100 rabbits, how many days would it take for Wendi's rabbits to clear all the grass off of her grassland property?"""
    land_area = 200 * 900  # in square feet
    rabbit_graze_area = 10 * 9  # in square feet, assuming 1 yard = 3 feet
    no_of_rabbits = 100
    daily_graze_area = no_of_rabbits * rabbit_graze_area  # in square feet
    days_to_clear_all_grass = land_area // daily_graze_area
    result = days_to_clear_all_grass
    return result

print(solution())