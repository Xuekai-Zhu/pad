def solution():
    """Tommy is making 12 loaves of bread. He needs 4 pounds of flour per loaf. A 10-pound bag of flour costs $10 and a 12-pound bag costs $13. When he is done making his bread, he has no use for flour and so he will throw away whatever is left. How much does he spend on flour if he buys the cheapest flour to get enough?"""
    loaves_of_bread = 12
    pounds_of_flour_per_loaf = 4
    total_pounds_of_flour = loaves_of_bread * pounds_of_flour_per_loaf

    # Cost of a 10-pound bag of flour
    cost_of_10lb_bag_of_flour = 10
    pounds_of_flour_in_10lb_bag = 10
    num_10lb_bags = total_pounds_of_flour // pounds_of_flour_in_10lb_bag
    remaining_pounds = total_pounds_of_flour % pounds_of_flour_in_10lb_bag
    cost_of_needed_10lb_bags = num_10lb_bags * cost_of_10lb_bag_of_flour

    # Cost of a 12-pound bag of flour
    cost_of_12lb_bag_of_flour = 13
    pounds_of_flour_in_12lb_bag = 12
    num_12lb_bags = remaining_pounds // pounds_of_flour_in_12lb_bag
    cost_of_needed_12lb_bags = num_12lb_bags * cost_of_12lb_bag_of_flour

    total_cost = cost_of_needed_10lb_bags + cost_of_needed_12lb_bags
    result = total_cost
    return result

print(solution())