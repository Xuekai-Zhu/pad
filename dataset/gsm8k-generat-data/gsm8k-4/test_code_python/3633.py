def solution():
    """Marcy keeps a 2-liter bottle of water by her desk. She takes a sip every five minutes, and each sip is 40 ml. How many minutes does it take her to drink the whole bottle of water?"""
    # Define the volume of the water bottle and the volume of each sip
    water_volume = 2000  # in ml
    sip_volume = 40  # in ml

    # Calculate the number of sips needed to drink the entire bottle
    num_sips = water_volume / sip_volume

    # Calculate the total time in minutes needed to drink the entire bottle
    total_time = num_sips * 5

    # Display the result
    result = total_time
    return result

print(solution())