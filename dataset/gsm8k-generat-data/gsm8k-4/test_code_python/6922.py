def solution():
    """Wendi lives on a plot of land that is 200 feet by 900 feet of grassland. She raises rabbits on her property by allowing the rabbits to graze on the grass that grows on her land. If one rabbit can eat enough grass to clear ten square yards of lawn area per day, and Wendi owns 100 rabbits, how many days would it take for Wendi's rabbits to clear all the grass off of her grassland property?"""
    # Define the size of the grassland
    width = 200
    length = 900

    # Calculate the total area of grassland in square yards
    total_area = (width * length) / 9

    # Define the number of rabbits and the amount of grass they can clear each day
    rabbits = 100
    grass_cleared_per_rabbit = 10

    # Calculate the total amount of grass that can be cleared each day
    total_grass_cleared = rabbits * grass_cleared_per_rabbit

    # Calculate the number of days it would take to clear all the grassland
    days = total_area / total_grass_cleared

    result = round(days)
    return result

print(solution())