def solution():
    """Kim drinks a 1.5-quart bottle of water.  She then drinks a 12 ounce can of water.  How many ounces of water did she drink?"""
    # Define the total amount of water
    total_water = 0
    
    # Calculate and add the amount of water from the bottle
    bottle_water = 1.5 * 32 # 1 quart = 32 ounces
    total_water += bottle_water
    
    # Add the amount of water from the can
    can_water = 12
    total_water += can_water
    
    # Display the total amount of water drank in ounces
    result = total_water
    return result

print(solution())