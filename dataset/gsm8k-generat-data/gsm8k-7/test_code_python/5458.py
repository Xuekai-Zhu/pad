def solution():
    num_barrels = 4
    cask_capacity = 20

    # Calculate the capacity of a barrel
    barrel_capacity = 2 * cask_capacity + 3

    # Calculate the total capacity of all barrels
    total_barrel_capacity = num_barrels * barrel_capacity

    # Calculate the total capacity of all barrels and the cask
    total_capacity = total_barrel_capacity + cask_capacity

    result = total_capacity
    return result

print(solution())