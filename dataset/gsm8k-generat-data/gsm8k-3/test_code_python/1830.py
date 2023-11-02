def solution():
    """Chad is hosting a BBQ on the hottest day of the year, where there will be a total of 15 people.  He will need 2 pounds of ice per person to account for the heat.  One pound bags of ice are sold for $3.00 for a pack of 10.  How much will he spend on ice?"""
    # Calculate the total amount of ice needed in pounds
    ice_needed = 15 * 2

    # Calculate the number of 10-pack bags of ice needed
    bags_needed = (ice_needed // 10) + 1 # round up to the nearest whole bag

    # Calculate the total cost of the ice
    cost = bags_needed * 3

    # Display the total cost of the ice
    result = cost
    return result

print(solution())