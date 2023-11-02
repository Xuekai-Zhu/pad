def solution():
    old_bridge_capacity = 2000
    new_bridge_capacity = 2 * old_bridge_capacity
    increase_percent = 0.6

    # Calculate the monthly number of vehicles passing through the new bridge
    new_bridge_passes = old_bridge_capacity * (1 + increase_percent)

    # Calculate the total number of vehicles passing through both bridges in one month
    total_passes_per_month = old_bridge_capacity + new_bridge_passes

    # Calculate the total number of passes in a year
    total_passes_per_year = total_passes_per_month * 12

    result = total_passes_per_year
    return result

print(solution())