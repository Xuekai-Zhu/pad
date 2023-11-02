def solution():
    """The country of Belize had a 5 lane bridge that had 2000 vehicles passing through it every month. They decided to build a new bridge that had twice the capacity of the old one, and the number of vehicles passing through the new one increased by 60% more than the old bridge. If the bridges work concurrently for a year, calculate the total number of vehicles that pass through the two bridges."""
    old_bridge_capacity = 2000 * 12
    new_bridge_capacity = 2 * 5 * 2000 * 1.6 * 12
    total_capacity = old_bridge_capacity + new_bridge_capacity
    result = total_capacity
    return result

print(solution())