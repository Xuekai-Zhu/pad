def solution():
    """The country of Belize had a 5 lane bridge that had 2000 vehicles passing through it every month. They decided to build a new bridge that had twice the capacity of the old one, and the number of vehicles passing through the new one increased by 60% more than the old bridge. If the bridges work concurrently for a year, calculate the total number of vehicles that pass through the two bridges."""
    # Define the number of vehicles passing through the old bridge per month
    old_bridge_monthly = 2000

    # Define the capacity of the new bridge relative to the old bridge
    new_bridge_capacity = 2

    # Define the percentage increase in traffic for the new bridge
    new_bridge_increase = 0.6

    # Calculate the number of vehicles passing through the new bridge per month
    new_bridge_monthly = old_bridge_monthly * new_bridge_capacity * (1 + new_bridge_increase)

    # Calculate the total number of vehicles passing through both bridges per month
    total_monthly = old_bridge_monthly + new_bridge_monthly

    # Calculate the total number of vehicles passing through both bridges per year
    total_yearly = total_monthly * 12

    result = total_yearly
    return result

print(solution())