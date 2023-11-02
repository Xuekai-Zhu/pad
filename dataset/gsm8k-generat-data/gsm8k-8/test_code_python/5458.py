def solution():
    # Calculate the capacity of one barrel
    cask_capacity = 20
    barrel_capacity = 2 * cask_capacity + 3

    # Calculate the total water storage capacity
    total_capacity = barrel_capacity * 4 + cask_capacity

    result = total_capacity
    return result

print(solution())