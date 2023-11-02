def solution():
    """One pair of pants requires 8.5 feet of fabric. Nguyen needs to make 7 pairs of pants for the wedding. He has 3.5 yards of fabric. How many feet of fabric does Nguyen still need for the pants?"""
    # Define the amount of fabric required per pair of pants and the number of pants needed
    FABRIC_PER_PANT = 8.5
    NUM_PANTS = 7

    # Convert the amount of available fabric from yards to feet
    fabric_available = 3.5 * 3

    # Calculate the total amount of fabric needed for the pants
    fabric_needed = FABRIC_PER_PANT * NUM_PANTS

    # Calculate the amount of fabric still needed
    fabric_still_needed = fabric_needed - fabric_available

    # Display the amount of fabric still needed
    result = fabric_still_needed
    return result

print(solution())