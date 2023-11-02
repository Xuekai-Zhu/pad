def solution():
    """Chad is hosting a BBQ on the hottest day of the year, where there will be a total of 15 people. He will need 2 pounds of ice per person to account for the heat. One pound bags of ice are sold for $3.00 for a pack of 10. How much will he spend on ice?"""
    people = 15
    ice_per_person = 2
    total_ice = people * ice_per_person
    ice_bags = total_ice / 10
    if ice_bags.is_integer():
        ice_bags = int(ice_bags)
    else:
        ice_bags = int(ice_bags) + 1
    cost_per_ice_bag = 3
    total_cost = ice_bags * cost_per_ice_bag
    result = total_cost
    return result

print(solution())