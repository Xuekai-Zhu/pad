def solution():
    """The country of Belize had a 5 lane bridge that had 2000 vehicles passing through it every month. They decided to build a new bridge that had twice the capacity of the old one, and the number of vehicles passing through the new one increased by 60% more than the old bridge. If the bridges work concurrently for a year, calculate the total number of vehicles that pass through the two bridges."""
    old_bridge_capacity = 2000 * 12  # total number of vehicles passing through old bridge in a year
    new_bridge_capacity = 2 * 5 * old_bridge_capacity  # capacity of new bridge twice that of old bridge
    new_bridge_traffic = old_bridge_capacity * (1 + 0.6)  # vehicles passing through new bridge increased by 60% more
    total_traffic = old_bridge_capacity + new_bridge_traffic
    result = total_traffic
    return result

print(solution())