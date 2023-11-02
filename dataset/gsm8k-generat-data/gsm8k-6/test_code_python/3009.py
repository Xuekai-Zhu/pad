def solution():
    old_bridge_capacity = 2000  # number of vehicles passing through the old bridge every month
    new_bridge_capacity = 2*old_bridge_capacity  # capacity of the new bridge is twice that of the old one
    new_bridge_increase = 0.6 * old_bridge_capacity  # increase in number of vehicles passing through the new bridge
    total_vehicles_through_new_bridge = (new_bridge_capacity + new_bridge_increase) * 12  # total number of vehicles passing through the new bridge in a year
    total_vehicles_through_old_bridge = old_bridge_capacity * 12  # total number of vehicles passing through the old bridge in a year
    total_vehicles = total_vehicles_through_new_bridge + total_vehicles_through_old_bridge  # total number of vehicles passing through both bridges in a year
    result = total_vehicles
    return result

print(solution())