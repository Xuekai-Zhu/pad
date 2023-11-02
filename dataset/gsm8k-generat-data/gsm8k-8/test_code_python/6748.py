def solution():
    # Define the number of whiskers for Juniper and calculate Puffy's and Scruffy's whiskers
    juniper_whiskers = 12
    puffy_whiskers = 3 * juniper_whiskers
    scruffy_whiskers = 2 * puffy_whiskers

    # Calculate the total number of whiskers for the four cats
    total_whiskers = puffy_whiskers + scruffy_whiskers + juniper_whiskers

    # Calculate the average number of whiskers for the three cats (excluding Buffy)
    average_whiskers = (total_whiskers - buffy_whiskers) / 3

    # Calculate Buffy's whiskers by setting up an equation
    buffy_whiskers = (total_whiskers - juniper_whiskers - puffy_whiskers - scruffy_whiskers) / 1

    result = buffy_whiskers
    return result

print(solution())