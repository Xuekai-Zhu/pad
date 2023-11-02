def solution():
    # Calculate the cost of ingredients for the blueberry pie
    blueberry_cost = 2 + 1 + 1.5 + ((3 * 16) / 8) * 2.25  # $2 for flour, $1 for sugar, $1.5 for eggs and butter, and cost of blueberries

    # Calculate the cost of ingredients for the cherry pie
    cherry_cost = 2 + 1 + 1.5 + (14 / 4)  # $2 for flour, $1 for sugar, $1.5 for eggs and butter, and cost of cherries

    # Determine which pie is cheaper
    if blueberry_cost < cherry_cost:
        cheapest_pie_cost = blueberry_cost
    else:
        cheapest_pie_cost = cherry_cost

    result = cheapest_pie_cost
    return result

print(solution())