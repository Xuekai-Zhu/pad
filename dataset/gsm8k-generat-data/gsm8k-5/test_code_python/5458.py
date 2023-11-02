def solution():
    cask_size = 20  # A cask can store 20 gallons of water
    barrel_size = 3 + 2 * cask_size  # A barrel can store 3 gallons more than twice as much as a cask
    num_barrels = 4  # James has 4 barrels

    # Calculate the total water storage capacity
    total_capacity = cask_size + num_barrels * barrel_size
    result = total_capacity
    return result

print(solution())