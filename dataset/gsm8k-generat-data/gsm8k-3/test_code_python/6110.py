def solution():
    """Ginger ended up working 8 hours outside in her garden.  She kept a water bottle with her that held 2 cups of water.  She drank a full bottle of every hour she was outside.  She also poured an additional 5 bottles of water over the new plants she planted.  How many cups of water did Ginger drink/use that day?"""
    # Define the amount of water Ginger's water bottle holds
    BOTTLE_SIZE = 2

    # Calculate the number of water bottles Ginger drank
    num_bottles = 8

    # Calculate the total amount of water Ginger drank
    water_drunk = num_bottles * BOTTLE_SIZE

    # Calculate the amount of water Ginger used to water the new plants
    water_used = 5 * BOTTLE_SIZE

    # Calculate the total amount of water Ginger drank/used
    total_water = water_drunk + water_used

    # Display the total amount of water
    result = total_water
    return result

print(solution())