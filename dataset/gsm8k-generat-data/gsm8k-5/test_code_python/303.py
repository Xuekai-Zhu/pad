def solution():
    loaves_of_bread = 12  # Tommy is making 12 loaves of bread
    flour_per_loaf = 4  # Tommy needs 4 pounds of flour per loaf

    # Calculate the total amount of flour needed
    total_flour = loaves_of_bread * flour_per_loaf

    # Calculate the cost of buying a 10-pound bag of flour
    cost_10lb_bag = 10
    pounds_in_10lb_bag = 10
    cost_per_pound_10lb = cost_10lb_bag / pounds_in_10lb_bag

    # Calculate the cost of buying a 12-pound bag of flour
    cost_12lb_bag = 13
    pounds_in_12lb_bag = 12
    cost_per_pound_12lb = cost_12lb_bag / pounds_in_12lb_bag

    # Buy the cheapest flour to get enough
    if total_flour <= pounds_in_10lb_bag:
        total_cost = total_flour * cost_per_pound_10lb
    else:
        num_12lb_bags = total_flour // pounds_in_12lb_bag
        num_10lb_bags = (total_flour % pounds_in_12lb_bag) / pounds_in_10lb_bag
        total_cost = (num_12lb_bags * cost_12lb_bag) + (num_10lb_bags * cost_10lb_bag)

    result = total_cost
    return result

print(solution())