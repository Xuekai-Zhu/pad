def solution():
    """James has barrels that he uses to store water. They store 3 gallons more than twice as much as a large cask. If he has 4 barrels and a cask stores 20 gallons, how much water can he store?"""
    cask_size = 20
    barrel_size = 2 * cask_size + 3
    num_barrels = 4
    total_water = cask_size + num_barrels * barrel_size
    result = total_water
    return result

print(solution())