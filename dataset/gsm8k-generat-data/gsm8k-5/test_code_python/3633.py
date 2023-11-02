def solution():
    bottle_size = 2 * 1000  # Marcy has a 2-liter bottle of water, converted to milliliters
    sip_size = 40  # Marcy takes a sip of 40 ml every 5 minutes

    # Calculate the total number of sips needed to finish the bottle
    total_sips = bottle_size / sip_size

    # Calculate the total number of minutes needed to finish the bottle
    total_minutes = total_sips * 5
    result = total_minutes
    return result

print(solution())