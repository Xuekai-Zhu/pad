def solution():
    """Tommy is making 12 loaves of bread. He needs 4 pounds of flour per loaf. A 10-pound bag of flour costs $10 and a 12-pound bag costs $13. When he is done making his bread, he has no use for flour and so he will throw away whatever is left. How much does he spend on flour if he buys the cheapest flour to get enough?"""
    # Define the amount of flour needed in pounds
    flour_needed = 12 * 4

    # Calculate the cost of buying a 10-pound bag of flour
    cost_10pound = 10
    flour_10pound = 10

    # Calculate the cost of buying a 12-pound bag of flour
    cost_12pound = 13
    flour_12pound = 12

    # Choose the cheapest option that provides enough flour
    if flour_needed <= flour_10pound:
        total_cost = cost_10pound
    else:
        # Calculate how many bags of 12-pound flour are needed
        bags_12pound = flour_needed // flour_12pound
        if flour_needed % flour_12pound != 0:
            bags_12pound += 1

        # Calculate the total cost of buying the necessary amount of flour
        total_cost = bags_12pound * cost_12pound

    result = total_cost
    return result

print(solution())