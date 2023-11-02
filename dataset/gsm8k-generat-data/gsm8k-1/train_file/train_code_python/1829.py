def solution():
    """Chad is hosting a BBQ on the hottest day of the year, where there will be a total of 15 people. He will need 2 pounds of ice per person to account for the heat. One pound bags of ice are sold for $3.00 for a pack of 10. How much will he spend on ice?"""
    people = 15
    pounds_per_person = 2
    total_pounds = people * pounds_per_person
    bags_needed = total_pounds / 10
    cost_per_bag = 3
    total_cost = bags_needed * cost_per_bag
    result = total_cost
    return result

print(solution())