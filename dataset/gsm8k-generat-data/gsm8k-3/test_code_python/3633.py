def solution():
    """Marcy keeps a 2-liter bottle of water by her desk. She takes a sip every five minutes, and each sip is 40 ml. How many minutes does it take her to drink the whole bottle of water?"""
    # Define the volume of the water bottle in milliliters
    BOTTLE_SIZE = 2000

    # Define the volume of each sip in milliliters
    SIP_SIZE = 40

    # Calculate the number of sips required to empty the bottle
    sips = BOTTLE_SIZE / SIP_SIZE

    # Calculate the time required to empty the bottle in minutes
    time = sips * 5

    # Display the time required to empty the bottle
    result = time
    return result

print(solution())