def solution():
    """Ginger ended up working 8 hours outside in her garden. She kept a water bottle with her that held 2 cups of water. She drank a full bottle every hour she was outside. She also poured an additional 5 bottles of water over the new plants she planted. How many cups of water did Ginger drink/use that day?"""
    # Define the number of hours Ginger worked outside
    hours_worked = 8

    # Define the size of Ginger's water bottle in cups
    bottle_size = 2

    # Calculate the number of water bottles Ginger drank
    bottles_drank = hours_worked

    # Calculate the total cups of water Ginger drank
    water_drank = bottles_drank * bottle_size

    # Calculate the cups of water Ginger used for the plants
    water_used = 5 * bottle_size

    # Calculate the total cups of water Ginger used
    total_water_used = water_drank + water_used

    # return the result
    result = total_water_used
    return result

print(solution())