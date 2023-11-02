def solution():
    """The country of Belize had a 5 lane bridge that had 2000 vehicles passing through it every month. They decided to build a new bridge that had twice the capacity of the old one, and the number of vehicles passing through the new one increased by 60% more than the old bridge. If the bridges work concurrently for a year, calculate the total number of vehicles that pass through the two bridges."""
    
    # Define the variables for the old bridge
    old_lanes = 5
    old_capacity = 2000
    old_total = old_lanes * old_capacity

    # Define the variables for the new bridge
    new_lanes = 10
    new_capacity = old_capacity * 2
    new_increase = old_capacity * 0.6
    new_total = new_lanes * (new_capacity + new_increase)

    # Calculate the total number of vehicles passing through both bridges in a year
    total = (old_total + new_total) * 12

    # Display the total number of vehicles passing through both bridges
    result = total
    return result

print(solution())