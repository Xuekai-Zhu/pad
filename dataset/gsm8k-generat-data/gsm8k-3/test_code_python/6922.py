def solution():
    """Wendi lives on a plot of land that is 200 feet by 900 feet of grassland. She raises rabbits on her property by allowing the rabbits to graze on the grass that grows on her land. If one rabbit can eat enough grass to clear ten square yards of lawn area per day, and Wendi owns 100 rabbits, how many days would it take for Wendi's rabbits to clear all the grass off of her grassland property?"""
    # Calculate the total area of the grassland in square yards
    grassland_area = (200 * 900) / 9

    # Calculate the total area that Wendi's rabbits can clear per day
    rabbit_area_per_day = 100 * 10

    # Calculate the number of days it would take for the rabbits to clear all the grass
    days_to_clear = grassland_area / rabbit_area_per_day

    # Display the number of days
    result = days_to_clear
    return result

print(solution())