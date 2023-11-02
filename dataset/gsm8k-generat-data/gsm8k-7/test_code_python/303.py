def solution():
    num_loaves = 12
    flour_per_loaf = 4  # pounds

    # Calculate the total amount of flour needed in pounds
    total_flour = num_loaves * flour_per_loaf

    # Calculate the cost of a 10-pound bag of flour
    cost_10lb_flour = 10

    # Calculate the cost of a 12-pound bag of flour
    cost_12lb_flour = 13

    # Calculate how many bags of flour Tommy needs to buy and round up to the nearest whole number
    num_12lb_bags = math.ceil(total_flour / 12)

    # Calculate the cost of the cheapest flour option
    cost_cheapest_flour = min(num_12lb_bags * cost_12lb_flour, (num_12lb_bags - 1) * cost_12lb_flour + cost_10lb_flour)

    result = cost_cheapest_flour
    return result

print(solution())