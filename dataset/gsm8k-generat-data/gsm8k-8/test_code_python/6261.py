def solution():
    # Define the total cost of Peter's purchase and the total number of items
    peter_cost = 62
    peter_items = 2 + 5

    # Define the total cost of Jessica's purchase and the total number of items
    jessica_cost = 20
    jessica_items = 2

    # Calculate the cost per item for each purchase
    peter_cost_per_item = peter_cost / peter_items
    jessica_cost_per_item = jessica_cost / jessica_items

    # Calculate the cost per pair of pants
    cost_per_pants = (2 * peter_cost_per_item - 5 * jessica_cost_per_item) / 2
    result = cost_per_pants
    return result

print(solution())