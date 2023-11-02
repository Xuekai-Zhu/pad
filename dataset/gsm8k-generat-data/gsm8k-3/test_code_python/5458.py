def solution():
    """James has barrels that he uses to store water.  They store 3 gallons more than twice as much as a large cask.  If he has 4 barrels and a cask stores 20 gallons, how much water can he store?"""
    # Define the capacity of a large cask
    CASK_CAPACITY = 20

    # Calculate the capacity of one barrel
    barrel_capacity = 2 * CASK_CAPACITY + 3

    # Calculate the total capacity of all the barrels
    total_capacity = barrel_capacity * 4

    # Add the capacity of the large cask to the total capacity
    total_capacity += CASK_CAPACITY

    # Display the total capacity
    result = total_capacity
    return result

print(solution())