def solution():
    # Calculate the cost of blueberries for the blueberry pie
    blueberry_cost = (3 * 16 / 8) * 2.25

    # Calculate the cost of cherries for the cherry pie
    cherry_cost = 14

    # Calculate the total cost of ingredients for each pie
    blueberry_total_cost = 2 + 1 + 1.5 + blueberry_cost
    cherry_total_cost = 2 + 1 + 1.5 + cherry_cost

    # Choose the cheapest pie
    if blueberry_total_cost < cherry_total_cost:
        cheapest_pie_cost = blueberry_total_cost
    else:
        cheapest_pie_cost = cherry_total_cost

    result = cheapest_pie_cost
    return result

print(solution())