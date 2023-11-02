def solution():
    # Ingredients for the crust
    flour_cost = 2
    sugar_cost = 1
    eggs_butter_cost = 1.5
    crust_total_cost = flour_cost + sugar_cost + eggs_butter_cost

    # Blueberry pie ingredients
    blueberry_cost_per_container = 2.25
    blueberry_num_containers = 3 / 0.5 # 3 pounds convert to 24 ounces
    blueberry_total_cost = blueberry_cost_per_container * blueberry_num_containers
    blueberry_total_cost += crust_total_cost

    # Cherry pie ingredients
    cherry_cost_per_bag = 14
    cherry_num_bags = 4
    cherry_total_cost = cherry_cost_per_bag / cherry_num_bags
    cherry_total_cost += crust_total_cost

    # Determine which pie is cheapest
    if blueberry_total_cost < cherry_total_cost:
        result = blueberry_total_cost
    else:
        result = cherry_total_cost

    return result

print(solution())