def solution():
    """Chad is hosting a BBQ on the hottest day of the year, where there will be a total of 15 people.  He will need 2 pounds of ice per person to account for the heat.  One pound bags of ice are sold for $3.00 for a pack of 10.  How much will he spend on ice?"""
    # Define the total number of people and the amount of ice needed per person
    total_people = 15
    ice_needed = 2 * total_people

    # Calculate the number of bags of ice needed
    bags_needed = ice_needed / 10
    bags_needed = round(bags_needed + 0.5)

    # Calculate the total cost of the ice
    cost = bags_needed * 3.00

    # Return the result
    result = cost
    return result

print(solution())