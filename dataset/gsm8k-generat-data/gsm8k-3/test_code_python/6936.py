def solution():
    """Gary is restocking the grocery produce section. He adds 60 bundles of asparagus at $3.00 each, 40 boxes of grapes at $2.50 each, and 700 apples at $0.50 each. How much is all the produce he stocked worth?"""
    # Define the price of each type of produce
    ASPARAGUS_PRICE = 3.0
    GRAPES_PRICE = 2.5
    APPLES_PRICE = 0.5

    # Define the quantity of each type of produce
    asparagus_bundles = 60
    grape_boxes = 40
    apples = 700

    # Calculate the total cost of the asparagus
    asparagus_cost = asparagus_bundles * ASPARAGUS_PRICE

    # Calculate the total cost of the grapes
    grapes_cost = grape_boxes * GRAPES_PRICE

    # Calculate the total cost of the apples
    apples_cost = apples * APPLES_PRICE

    # Calculate the total cost of all the produce
    total_cost = asparagus_cost + grapes_cost + apples_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())