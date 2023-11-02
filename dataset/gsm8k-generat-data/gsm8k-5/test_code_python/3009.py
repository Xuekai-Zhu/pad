def solution():
    old_bridge_capacity = 2000  # The old bridge had a capacity of 2000 vehicles per month
    new_bridge_capacity = old_bridge_capacity * 2  # The new bridge has twice the capacity of the old one
    new_bridge_traffic_increase = 0.6 * old_bridge_capacity  # The new bridge has 60% more traffic than the old one
    total_traffic = 12 * (old_bridge_capacity + new_bridge_capacity + new_bridge_traffic_increase)  # Both bridges work concurrently for a year, so multiply monthly traffic by 12

    result = total_traffic
    return result

print(solution())