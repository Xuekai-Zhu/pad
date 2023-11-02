def solution():
    # Calculate the number of vehicles passing through the old bridge annually
    old_bridge_annual = 2000 * 12

    # Calculate the capacity of the new bridge
    new_bridge_capacity = 2 * 2000

    # Calculate the increase in the number of vehicles passing through the new bridge
    new_bridge_increase = 0.6 * 2000

    # Calculate the number of vehicles passing through the new bridge annually
    new_bridge_annual = (2000 + new_bridge_increase) * 12

    # Calculate the total number of vehicles passing through the two bridges
    total_vehicles = old_bridge_annual + new_bridge_annual
    result = total_vehicles
    return result

print(solution())