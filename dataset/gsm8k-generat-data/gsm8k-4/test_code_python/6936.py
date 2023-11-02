def solution():
    """Gary is restocking the grocery produce section. He adds 60 bundles of asparagus at $3.00 each, 40 boxes of grapes at $2.50 each, and 700 apples at $0.50 each. How much is all the produce he stocked worth?"""
    # Define the prices and quantities of each type of produce
    asparagus_price = 3.00
    asparagus_quantity = 60
    grapes_price = 2.50
    grapes_quantity = 40
    apples_price = 0.50
    apples_quantity = 700

    # Calculate the total value of each type of produce
    asparagus_value = asparagus_price * asparagus_quantity
    grapes_value = grapes_price * grapes_quantity
    apples_value = apples_price * apples_quantity

    # Calculate the total value of all the produce
    total_value = asparagus_value + grapes_value + apples_value

    # Return the result
    result = total_value
    return result

print(solution())