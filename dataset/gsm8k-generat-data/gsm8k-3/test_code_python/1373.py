def solution():
    """Jose bought 20,000 square meters of land and needs to divide it equally with his four siblings. How much land, in the square meters, will Jose have after dividing it with his siblings?"""
    # Define the number of siblings including Jose
    NUM_SIBLINGS = 5

    # Calculate the amount of land each sibling will have
    land_per_sibling = 20000 / NUM_SIBLINGS

    # Calculate the amount of land that Jose will have after dividing with his siblings
    jose_land = land_per_sibling

    # Display the amount of land that Jose will have
    result = jose_land
    return result

print(solution())