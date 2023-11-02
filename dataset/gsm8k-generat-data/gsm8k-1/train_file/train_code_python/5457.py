def solution():
    """James has barrels that he uses to store water. They store 3 gallons more than twice as much as a large cask. If he has 4 barrels and a cask stores 20 gallons, how much water can he store?"""
    cask_capacity = 20
    barrel_capacity = 2*cask_capacity + 3
    total_barrels = 4
    total_capacity = barrel_capacity * total_barrels
    result = total_capacity
    return result

print(solution())