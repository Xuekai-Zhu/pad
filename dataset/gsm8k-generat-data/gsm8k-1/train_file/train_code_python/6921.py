def solution():
    """Wendi lives on a plot of land that is 200 feet by 900 feet of grassland. She raises rabbits on her property by allowing the rabbits to graze on the grass that grows on her land. If one rabbit can eat enough grass to clear ten square yards of lawn area per day, and Wendi owns 100 rabbits, how many days would it take for Wendi's rabbits to clear all the grass off of her grassland property?"""
    land_length = 900
    land_width = 200
    land_area = land_length * land_width
    rabbit_grazing_area_per_day = 10*(1/9) # 1 square yard = 9 square feet
    total_rabbit_grazing_area_per_day = rabbit_grazing_area_per_day * 100
    days_to_clear_grass = land_area / total_rabbit_grazing_area_per_day
    result = days_to_clear_grass
    return result

print(solution())