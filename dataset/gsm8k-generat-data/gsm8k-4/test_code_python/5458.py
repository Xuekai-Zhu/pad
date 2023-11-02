def solution():
    """James has barrels that he uses to store water. They store 3 gallons more than twice as much as a large cask. If he has 4 barrels and a cask stores 20 gallons, how much water can he store?"""
    # Define the amount of water a cask can store
    cask_capacity = 20

    # Calculate the capacity of each barrel
    barrel_capacity = 2*cask_capacity + 3

    # Calculate the total capacity of all the barrels
    total_barrel_capacity = 4 * barrel_capacity

    # Calculate the total capacity of all the storage containers
    total_capacity = total_barrel_capacity + cask_capacity

    result = total_capacity
    return result

print(solution())